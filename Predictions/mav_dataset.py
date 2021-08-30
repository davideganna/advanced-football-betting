import pandas as pd
import Models
import DictsAndLists as DAL
import backtesting
import logging, coloredlogs

pd.set_option('display.max_rows', 1000)

# ------ Logger ------- #
logger = logging.getLogger('build_moving_average_model.py')
coloredlogs.install(level='INFO', logger=logger)

# Only the most significant features will be considered
away_features = Models.away_features
home_features = Models.home_features
features = Models.features

# To evaluate accuracy
dates_list  = []
predictions = []
true_values = []
model_prob  = []
model_odds  = []
odds_winner = []
odds_loser  = []
home_teams_list   = []
away_teams_list   = []
winners_list = []

def extract_and_insert(next_game, _df, average_N, evaluated_indexes, to_insert_list, winners_list):
    """
    Based on the next game, the function computes the average of N the previous games played by 
        the same team and inserts the values in "averageN_season.csv".
    """
    # Extract away_team Name and home_team Name from last_N_games_away and last_N_games_home
    away_team = next_game['AwayTeam'].values[0]
    home_team = next_game['HomeTeam'].values[0]

    # Before predicting a game, check that it has not yet been predicted.
    # This is the case where e.g., TeamHome's next game at home against TeamAway has been evaluated ...
    # by both next home game and next away game. They are the same game, which are therefore predicted twice. 
    if next_game.index[0] not in evaluated_indexes:
        # Track the inserted game based on its index
        evaluated_indexes.append(next_game.index[0])

        # Extract indexes for last N games
        all_games_away_indexes = _df.loc[_df['AwayTeam'] == away_team].index
        all_games_home_indexes = _df.loc[_df['HomeTeam'] == home_team].index
        next_away_indexes_reduced = [x for x in all_games_away_indexes if x < next_game.index[0]][-average_N:]
        next_home_indexes_reduced = [x for x in all_games_home_indexes if x < next_game.index[0]][-average_N:]

        # Extract last N games based on indexes
        last_N_games_away = _df.iloc[next_away_indexes_reduced]
        last_N_games_home = _df.iloc[next_home_indexes_reduced]

        # Concatenate the two teams with their average stats
        to_insert = pd.concat(
            [
                round(last_N_games_away[away_features].mean(),5), 
                round(last_N_games_home[home_features].mean(),5)
            ],
            axis=0)[features]

        to_insert_list.append(to_insert)
        winners_list.append(_df['Winner'].loc[_df.index == next_game.index[0]].values[0])


def build_moving_average_dataset(average_N, skip_n):
    # England
    e0_2016 = pd.read_csv('past_data/England/E0_2016.csv')
    e0_2017 = pd.read_csv('past_data/England/E0_2017.csv')
    e0_2018 = pd.read_csv('past_data/England/E0_2018.csv')
    e0_2019 = pd.read_csv('past_data/England/E0_2019.csv')
    e0_2020 = pd.read_csv('past_data/England/E0_2020.csv')

    # Germany
    d1_2016 = pd.read_csv('past_data/Germany/D1_2016.csv')
    d1_2017 = pd.read_csv('past_data/Germany/D1_2017.csv')
    d1_2018 = pd.read_csv('past_data/Germany/D1_2018.csv')
    d1_2019 = pd.read_csv('past_data/Germany/D1_2019.csv')
    d1_2020 = pd.read_csv('past_data/Germany/D1_2020.csv')

    # Italy
    i1_2016 = pd.read_csv('past_data/Italy/I1_2016.csv')
    i1_2017 = pd.read_csv('past_data/Italy/I1_2017.csv')
    i1_2018 = pd.read_csv('past_data/Italy/I1_2018.csv')
    i1_2019 = pd.read_csv('past_data/Italy/I1_2019.csv')

    # Spain
    sp1_2016 = pd.read_csv('past_data/Spain/SP1_2016.csv')
    sp1_2017 = pd.read_csv('past_data/Spain/SP1_2017.csv')
    sp1_2018 = pd.read_csv('past_data/Spain/SP1_2018.csv')
    sp1_2019 = pd.read_csv('past_data/Spain/SP1_2019.csv')
    sp1_2020 = pd.read_csv('past_data/Spain/SP1_2020.csv')

    seasons = [
        e0_2016, e0_2017, e0_2018, e0_2019, e0_2020,
        d1_2016, d1_2017, d1_2018, d1_2019, d1_2020,
        i1_2016, i1_2017, i1_2018, i1_2019, # i1_2020 to be backtested
        sp1_2016, sp1_2017, sp1_2018, sp1_2019, sp1_2020
    ]

    print(f'Averaging {len(seasons)} datasets. MA: {average_N} games, first {skip_n} games are skipped.')

    for _df in seasons:
        # Cleanup at every iteration
        evaluated_indexes = []
        to_insert_list = []
        winners_list = []
        teams = sorted(_df['HomeTeam'].unique())
        for skip_n_games in range(skip_n, 50-average_N):
            # Get next game based on next_game_index
            for team in teams:
                # Find all games where "team" plays away
                all_games_away_indexes = _df.loc[_df['AwayTeam'] == team].index
                if (average_N+skip_n_games-1) < len(all_games_away_indexes):
                    last_away_index = all_games_away_indexes[average_N+skip_n_games-1]
                else:
                    last_away_index = len(all_games_away_indexes)-1
                last_away_game = _df.loc[_df.index == last_away_index]
                # Check if there are more games past the current index 
                try:
                    DAL.last_home_away_index_dict[team][0] = last_away_game.index[0]
                except: 
                    pass
                if max(all_games_away_indexes) != DAL.last_home_away_index_dict[team][0]:
                    next_game_index = min(i for i in all_games_away_indexes[skip_n+average_N:] if i > last_away_game.index)
                    next_game = _df.loc[_df.index == next_game_index]

                    all_games_home_indexes = _df.loc[_df['HomeTeam'] == next_game['HomeTeam'].values[0]].index

                    if next_game_index in all_games_home_indexes[skip_n+average_N:]:
                        extract_and_insert(next_game, _df, average_N, evaluated_indexes, to_insert_list, winners_list)
                        
                # Find all games where "team" plays home
                all_games_home_indexes = _df.loc[_df['HomeTeam'] == team].index
                if (average_N+skip_n_games-1) < len(all_games_home_indexes):
                    last_home_index = all_games_home_indexes[average_N+skip_n_games-1]
                else:
                    last_home_index = len(all_games_home_indexes)-1
                last_home_game = _df.loc[_df.index == last_home_index]
                # Check if there are more games past the current index 
                try:
                    DAL.last_home_away_index_dict[team][1] = last_home_game.index[0]
                except: 
                    pass
                if max(all_games_home_indexes) != DAL.last_home_away_index_dict[team][1]:
                    next_game_index = min(i for i in all_games_home_indexes[skip_n+average_N:] if i > last_home_game.index)
                    next_game = _df.loc[_df.index == next_game_index]
                    
                    all_games_away_indexes = _df.loc[_df['AwayTeam'] == next_game['AwayTeam'].values[0]].index
                    
                    if next_game_index in all_games_away_indexes[skip_n+average_N:]:
                        extract_and_insert(next_game, _df, average_N, evaluated_indexes, to_insert_list, winners_list)

        avg_df = pd.concat(to_insert_list, axis=1).transpose()
        avg_df['Winner'] = winners_list
        
        if _df is e0_2016:
            _df.name = '2016/2017 English Season DataFrame' 
            avg_df.to_csv('average_seasons/E0_2016.csv', index=False)
        elif _df is e0_2017:
            _df.name = '2017/2018 English Season DataFrame' 
            avg_df.to_csv('average_seasons/E0_2017.csv', index=False)
        elif _df is e0_2018:
            _df.name = '2018/2019 English Season DataFrame' 
            avg_df.to_csv('average_seasons/E0_2018.csv', index=False)
        elif _df is e0_2019:
            _df.name = '2018/2019 English Season DataFrame' 
            avg_df.to_csv('average_seasons/E0_2019.csv', index=False)
        elif _df is e0_2020:
            _df.name = '2019/2020 English Season DataFrame' 
            avg_df.to_csv('average_seasons/E0_2020.csv', index=False)
        elif _df is d1_2016:
            _df.name = '2016/2017 German Season DataFrame' 
            avg_df.to_csv('average_seasons/D1_2016.csv', index=False)
        elif _df is d1_2017:
            _df.name = '2017/2018 German Season DataFrame' 
            avg_df.to_csv('average_seasons/D1_2017.csv', index=False)
        elif _df is d1_2018:
            _df.name = '2018/2019 German Season DataFrame' 
            avg_df.to_csv('average_seasons/D1_2018.csv', index=False)
        elif _df is d1_2019:
            _df.name = '2018/2019 German Season DataFrame' 
            avg_df.to_csv('average_seasons/D1_2019.csv', index=False)
        elif _df is d1_2020:
            _df.name = '2019/2020 German Season DataFrame' 
            avg_df.to_csv('average_seasons/D1_2020.csv', index=False)
        elif _df is i1_2016:
            _df.name = '2016/2017 Italian Season DataFrame' 
            avg_df.to_csv('average_seasons/I1_2016.csv', index=False)
        elif _df is i1_2017:
            _df.name = '2017/2018 Italian Season DataFrame' 
            avg_df.to_csv('average_seasons/I1_2017.csv', index=False)
        elif _df is i1_2018:
            _df.name = '2018/2019 Italian Season DataFrame' 
            avg_df.to_csv('average_seasons/I1_2018.csv', index=False)
        elif _df is i1_2019:
            _df.name = '2018/2019 Italian Season DataFrame' 
            avg_df.to_csv('average_seasons/I1_2019.csv', index=False)
        elif _df is sp1_2016:
            _df.name = '2016/2017 Spanish Season DataFrame' 
            avg_df.to_csv('average_seasons/SP1_2016.csv', index=False)
        elif _df is sp1_2017:
            _df.name = '2017/2018 Spanish Season DataFrame' 
            avg_df.to_csv('average_seasons/SP1_2017.csv', index=False)
        elif _df is sp1_2018:
            _df.name = '2018/2019 Spanish Season DataFrame' 
            avg_df.to_csv('average_seasons/SP1_2018.csv', index=False)
        elif _df is sp1_2019:
            _df.name = '2018/2019 Spanish Season DataFrame' 
            avg_df.to_csv('average_seasons/SP1_2019.csv', index=False)
        elif _df is sp1_2020:
            _df.name = '2019/2020 Spanish Season DataFrame' 
            avg_df.to_csv('average_seasons/SP1_2020.csv', index=False)

        logger.info(f'Retrieved stats for {_df.name}')

    # Concatenate the 3 average season datasets
    avg_e0_2016 = pd.read_csv('average_seasons/E0_2016.csv')
    avg_e0_2017 = pd.read_csv('average_seasons/E0_2017.csv')
    avg_e0_2018 = pd.read_csv('average_seasons/E0_2018.csv')
    avg_e0_2019 = pd.read_csv('average_seasons/E0_2019.csv')
    avg_e0_2020 = pd.read_csv('average_seasons/E0_2020.csv')
    avg_d1_2016 = pd.read_csv('average_seasons/D1_2016.csv')
    avg_d1_2017 = pd.read_csv('average_seasons/D1_2017.csv')
    avg_d1_2018 = pd.read_csv('average_seasons/D1_2018.csv')
    avg_d1_2019 = pd.read_csv('average_seasons/D1_2019.csv')
    avg_d1_2020 = pd.read_csv('average_seasons/D1_2020.csv')
    avg_i1_2016 = pd.read_csv('average_seasons/I1_2016.csv')
    avg_i1_2017 = pd.read_csv('average_seasons/I1_2017.csv')
    avg_i1_2018 = pd.read_csv('average_seasons/I1_2018.csv')
    avg_i1_2019 = pd.read_csv('average_seasons/I1_2019.csv')
    avg_sp1_2016 = pd.read_csv('average_seasons/SP1_2016.csv')
    avg_sp1_2017 = pd.read_csv('average_seasons/SP1_2017.csv')
    avg_sp1_2018 = pd.read_csv('average_seasons/SP1_2018.csv')
    avg_sp1_2019 = pd.read_csv('average_seasons/SP1_2019.csv')
    avg_sp1_2020 = pd.read_csv('average_seasons/SP1_2020.csv')

    avg_total_df = pd.concat([
        avg_e0_2016, avg_e0_2017, avg_e0_2018, avg_e0_2019, avg_e0_2020,
        avg_d1_2016, avg_d1_2017, avg_d1_2018, avg_d1_2019, avg_d1_2020,
        avg_i1_2016, avg_i1_2017, avg_i1_2018, avg_i1_2019, # We predict i1_2020
        avg_sp1_2016, avg_sp1_2017, avg_sp1_2018, avg_sp1_2019, avg_sp1_2020,
    ], axis=0)

    avg_total_df.to_csv('merged_datasets/average_N_EDISp.csv', index=False)