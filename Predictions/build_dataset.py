import pandas as pd

def add_winner_to_df(df, file_path):
    """ 
    Create a column containing the winner:
    HomeTeam = 1
    Draw = 0
    AwayTeam = -1 
    """
    df = df.assign(Winner = 1)
    df['Winner'].loc[df['FTAG'] > df['FTHG']] = -1
    df['Winner'].loc[df['FTAG'] == df['FTHG']] = 0
    df.to_csv(file_path, index=False)


# Options
pd.set_option('display.max_rows', 500)
pd.options.mode.chained_assignment = None  # default='warn'

# England
e0_2016 = pd.read_csv('past_data/England/E0_2016.csv')
add_winner_to_df(e0_2016, 'past_data/England/E0_2016.csv')
e0_2017 = pd.read_csv('past_data/England/E0_2017.csv')
add_winner_to_df(e0_2017, 'past_data/England/E0_2017.csv')
e0_2018 = pd.read_csv('past_data/England/E0_2018.csv')
add_winner_to_df(e0_2018, 'past_data/England/E0_2018.csv')
e0_2019 = pd.read_csv('past_data/England/E0_2019.csv')
add_winner_to_df(e0_2019, 'past_data/England/E0_2019.csv')
e0_2020 = pd.read_csv('past_data/England/E0_2020.csv')
add_winner_to_df(e0_2020, 'past_data/England/E0_2020.csv')

england_df = pd.concat([e0_2016, e0_2017, e0_2018, e0_2019, e0_2020]).reset_index(drop=True)

# Germany
d1_2016 = pd.read_csv('past_data/Germany/D1_2016.csv')
add_winner_to_df(d1_2016, 'past_data/Germany/D1_2016.csv')
d1_2017 = pd.read_csv('past_data/Germany/D1_2017.csv')
add_winner_to_df(d1_2017, 'past_data/Germany/D1_2017.csv')
d1_2018 = pd.read_csv('past_data/Germany/D1_2018.csv')
add_winner_to_df(d1_2018, 'past_data/Germany/D1_2018.csv')
d1_2019 = pd.read_csv('past_data/Germany/D1_2019.csv')
add_winner_to_df(d1_2019, 'past_data/Germany/D1_2019.csv')
d1_2020 = pd.read_csv('past_data/Germany/D1_2020.csv')
add_winner_to_df(d1_2020, 'past_data/Germany/D1_2020.csv')

germany_df = pd.concat([d1_2016, d1_2017, d1_2018, d1_2019, d1_2020]).reset_index(drop=True)

# Italy
i1_2016 = pd.read_csv('past_data/Italy/I1_2016.csv')
add_winner_to_df(i1_2016, 'past_data/Italy/I1_2016.csv')
i1_2017 = pd.read_csv('past_data/Italy/I1_2017.csv')
add_winner_to_df(i1_2017, 'past_data/Italy/I1_2017.csv')
i1_2018 = pd.read_csv('past_data/Italy/I1_2018.csv')
add_winner_to_df(i1_2018, 'past_data/Italy/I1_2018.csv')
i1_2019 = pd.read_csv('past_data/Italy/I1_2019.csv')
add_winner_to_df(i1_2019, 'past_data/Italy/I1_2019.csv')
i1_2020 = pd.read_csv('past_data/Italy/I1_2020.csv')
add_winner_to_df(i1_2020, 'past_data/Italy/I1_2020.csv')

italy_df = pd.concat([i1_2016, i1_2017, i1_2018, i1_2019, i1_2020]).reset_index(drop=True)

# Spain
sp1_2016 = pd.read_csv('past_data/Spain/SP1_2016.csv')
add_winner_to_df(sp1_2016, 'past_data/Spain/SP1_2016.csv')
sp1_2017 = pd.read_csv('past_data/Spain/SP1_2017.csv')
add_winner_to_df(sp1_2017, 'past_data/Spain/SP1_2017.csv')
sp1_2018 = pd.read_csv('past_data/Spain/SP1_2018.csv')
add_winner_to_df(sp1_2018, 'past_data/Spain/SP1_2018.csv')
sp1_2019 = pd.read_csv('past_data/Spain/SP1_2019.csv')
add_winner_to_df(sp1_2019, 'past_data/Spain/SP1_2019.csv')
sp1_2020 = pd.read_csv('past_data/Spain/SP1_2020.csv')
add_winner_to_df(sp1_2020, 'past_data/Spain/SP1_2020.csv')

spain_df = pd.concat([sp1_2016, sp1_2017, sp1_2018, sp1_2019, sp1_2020]).reset_index(drop=True)

# Merge all the datasets
merged_df = pd.concat([england_df, germany_df, italy_df, spain_df]).reset_index(drop=True)
merged_df.drop(
    [
        'B365H',
        'B365D',
        'B365A',
        'BWH',
        'BWD',
        'BWA',
        'IWH',
        'IWD',
        'IWA',
        'PSH',
        'PSD',
        'PSA',
        'WHH',
        'WHD',
        'WHA',
        'VCH',
        'VCD',
        'VCA',
        'MaxH',
        'MaxD',
        'MaxA',
        'AvgH',
        'AvgD',
        'AvgA',
        'B365>2.5',
        'B365<2.5',
        'P>2.5',
        'P<2.5',
        'Max>2.5',
        'Max<2.5',
        'Avg>2.5',
        'Avg<2.5',
        'AHh',
        'B365AHH',
        'B365AHA',
        'PAHH',
        'PAHA',
        'MaxAHH',
        'MaxAHA',
        'AvgAHH',
        'AvgAHA',
        'B365CH',
        'B365CD',
        'B365CA',
        'BWCH',
        'BWCD',
        'BWCA',
        'IWCH',
        'IWCD',
        'IWCA',
        'PSCH',
        'PSCD',
        'PSCA',
        'WHCH',
        'WHCD',
        'WHCA',
        'VCCH',
        'VCCD',
        'VCCA',
        'MaxCH',
        'MaxCD',
        'MaxCA',
        'AvgCH',
        'AvgCD',
        'AvgCA',
        'B365C>2.5',
        'B365C<2.5',
        'PC>2.5',
        'PC<2.5',
        'MaxC>2.5',
        'MaxC<2.5',
        'AvgC>2.5',
        'AvgC<2.5',
        'AHCh',
        'B365CAHH',
        'B365CAHA',
        'PCAHH',
        'PCAHA',
        'MaxCAHH',
        'MaxCAHA',
        'AvgCAHH',
        'AvgCAHA',
        'LBH',
        'LBD',
        'LBA',
        'Bb1X2',
        'BbMxH',
        'BbAvH',
        'BbMxD',
        'BbAvD',
        'BbMxA',
        'BbAvA',
        'BbOU',
        'BbMx>2.5',
        'BbAv>2.5',
        'BbMx<2.5',
        'BbAv<2.5',
        'BbAH',
        'BbAHh',
        'BbMxAHH',
        'BbAvAHH',
        'BbMxAHA',
        'BbAvAHA',
        'Time',
        'Referee'
    ],
    axis=1,
    inplace=True
)
merged_df = merged_df.fillna(0)
# Assign the winner
# HomeTeam = 1
# Draw = 0
# AwayTeam = -1
merged_df = merged_df.assign(Winner = 1)
merged_df['Winner'].loc[merged_df['FTAG'] > merged_df['FTHG']] = -1
merged_df['Winner'].loc[merged_df['FTAG'] == merged_df['FTHG']] = 0
merged_df.to_csv('merged_datasets/merged_EDISp.csv', index=False)