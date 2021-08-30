import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('merged_datasets/merged_EDISp.csv')

# Define features and target
away_features = [
    'AS',
    'AST',
    'HTAG',
    'FTAG'
]

home_features = [
    'FTHG',
    'HTHG',
    'HST',
    'HS'
] 

target = ['Winner']
features = away_features + home_features

# Define a RF Classifier
X_train, y_train = df[features], df[target]
# Define a Random Forest Classifier
rf_clf = RandomForestClassifier(
    n_estimators=100, max_leaf_nodes=16, n_jobs=-1, random_state=42
)
rf_clf.fit(X_train, y_train.values.ravel())