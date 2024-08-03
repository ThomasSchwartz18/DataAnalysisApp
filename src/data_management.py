# src/data_management.py

import pandas as pd

#================================================================================================
# DATA CLEANING FUNCTIONS
#================================================================================================

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

#================================================================================================
# DATA MANIPULATION FUNCTIONS
#================================================================================================

def filter_data(df, condition):
    return df.query(condition)

def subset_data(df, columns):
    return df[columns]

def merge_data(df1, df2, on, how='inner'):
    return pd.merge(df1, df2, on=on, how=how)

def reshape_data(df, id_vars, value_vars, var_name, value_name):
    return pd.melt(df, id_vars=id_vars, value_vars=value_vars, var_name=var_name, value_name=value_name)

def pivot_data(df, index, columns, values):
    return df.pivot(index=index, columns=columns, values=values)

def add_calculated_field(df, field_name, calculation):
    df[field_name] = df.eval(calculation)
    return df
