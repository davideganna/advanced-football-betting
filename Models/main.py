#     /\      | |                             | | |  ____|        | | | |         | | | |  _ \     | | | | (_)            
#    /  \   __| |_   ____ _ _ __   ___ ___  __| | | |__ ___   ___ | |_| |__   __ _| | | | |_) | ___| |_| |_ _ _ __   __ _ 
#   / /\ \ / _` \ \ / / _` | '_ \ / __/ _ \/ _` | |  __/ _ \ / _ \| __| '_ \ / _` | | | |  _ < / _ \ __| __| | '_ \ / _` |
#  / ____ \ (_| |\ V / (_| | | | | (_|  __/ (_| | | | | (_) | (_) | |_| |_) | (_| | | | | |_) |  __/ |_| |_| | | | | (_| |
# /_/    \_\__,_| \_/ \__,_|_| |_|\___\___|\__,_| |_|  \___/ \___/ \__|_.__/ \__,_|_|_| |____/ \___|\__|\__|_|_| |_|\__, |
#                                                                                                                    __/ |
#                                                                                                                   |___/ 

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Options
pd.set_option('display.max_rows', 500)
pd.options.mode.chained_assignment = None  # default='warn'

# View most important features
df = pd.read_csv('merged_datasets/merged_EDISp.csv').fillna(0)
print(df)
# Assign the winner
# HomeTeam = 1
# Draw = 0
# AwayTeam = -1
df = df.assign(Winner = 1)
df['Winner'].loc[df['FTAG'] > df['FTHG']] = -1
df['Winner'].loc[df['FTAG'] == df['FTHG']] = 0

corr_matrix = df.corr()
#print(corr_matrix['Winner'].sort_values(ascending=False))


# Define features and target
features = [
    'FTHG',
    'HTHG',
    'HST',
    'HS',
    'AS',
    'AST',
    'HTAG',
    'FTAG',
] 

target = ['Winner']

# Define a RF Classifier
X_train, y_train = df[features], df[target]
# Define a Random Forest Classifier
rf_clf = RandomForestClassifier(
    n_estimators=100, max_leaf_nodes=16, n_jobs=-1, random_state=42
)
rf_clf.fit(X_train, y_train.values.ravel())

print(sorted(df['HomeTeam'].unique()))