# src/data_management.py

import pandas as pd

def impute_missing_values(df, strategy='mean'):
    if strategy == 'mean':
        return df.fillna(df.mean())
    elif strategy == 'median':
        return df.fillna(df.median())
    elif strategy == 'mode':
        return df.fillna(df.mode().iloc[0])
    else:
        raise ValueError("Strategy not recognized. Use 'mean', 'median', or 'mode'.")

def remove_duplicates(df):
    return df.drop_duplicates()

def validate_data(df, validation_rules):
    for column, rule in validation_rules.items():
        df = df[df[column].apply(rule)]
    return df

def scale_data(df):
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    return pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

def normalize_data(df):
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    return pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
