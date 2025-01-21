import pandas as pd

def string_normalization(df: pd.DataFrame, schema: dict = {}):
    for col, type in schema.items():
        if type == 'str':
            df[col] = df[col].str.upper()
    return df

def change_column_name(df: pd.DataFrame, schema_change: dict = {}):
    for key, val in schema_change.items():
        df[val] = df[key]
        df.drop([key], axis=1, inplace=True)
    return df

def handle_blanks(df: pd.DataFrame, schema: dict = {}):
    for key, type in schema.items():
        if type == 'int':
            df[key] = df[key].fillna(0).astype(int)

    return df

def coalesce_cols(df: pd.DataFrame):
    df['costo_vehiculo'] = df[['costo_vehiculo','costo_veiculo']].bfill(axis=1).iloc[:, 0]
    df.drop(['costo_veiculo'], axis=1, inplace=True)
    return df

def format_date(df: pd.DataFrame, schema: dict = {}):
    for col, type in schema.items():
        if type == 'date':
            df[col] = pd.to_datetime(df[col]).dt.strftime("%d-%m-%Y")
    return df

def calculations(df: pd.DataFrame, calculations: dict = {}):
    for col_name, calculation in calculations.items():
        df[col_name] = df.eval(f"{calculation}")
    return df