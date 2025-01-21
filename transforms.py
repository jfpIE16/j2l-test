import pandas as pd

def string_normalization(df: pd.DataFrame, schema: dict = {}):
    """
    String transformation.
    Args:
        df -> Pandas DataFrame
        schema -> Dictionary with schema information.

    Return:
        df -> Pandas DataFrame with transformed columns.
    """
    for col, type in schema.items():
        if type == 'str':
            df[col] = df[col].str.upper()
    return df

def change_column_name(df: pd.DataFrame, schema_change: dict = {}):
    """
    Column name
    Args:
        df -> Pandas DataFrame
        schema_change -> Dictionary with columns to rename.

    Return:
        df -> Pandas DataFrame with renamed columns.
    """
    for key, val in schema_change.items():
        df[val] = df[key]
        df.drop([key], axis=1, inplace=True)
    return df

def handle_blanks(df: pd.DataFrame, schema: dict = {}):
    """
    Blanks handling.
    Args:
        df -> Pandas DataFrame
        schema -> Dictionary with schema information.
    Usage: If the column in schema is of type int, then it will replace NULLS with 0.
    Return:
        df -> Pandas DataFrame with transformed columns.
    """
    for key, type in schema.items():
        if type == 'int':
            df[key] = df[key].fillna(0).astype(int)

    return df

def coalesce_cols(df: pd.DataFrame):
    """
    Blanks handling.
    Args:
        df -> Pandas DataFrame
    Usage: Coalesce columns costo_vehiculo, costo_veiculo maybe a typo in the creation of the JSON document.
    Return:
        df -> Pandas DataFrame with transformed columns.
    """
    df['costo_vehiculo'] = df[['costo_vehiculo','costo_veiculo']].bfill(axis=1).iloc[:, 0]
    df.drop(['costo_veiculo'], axis=1, inplace=True)
    return df

def format_date(df: pd.DataFrame, schema: dict = {}):
    """
    Date formatting.
    Args:
        df -> Pandas DataFrame
        schema -> Dictionary with schema information.
    Usage: If the column in schema is of type date, then it will formate the date as dd-mm-YYYY.
    Return:
        df -> Pandas DataFrame with transformed columns.
    """
    for col, type in schema.items():
        if type == 'date':
            df[col] = pd.to_datetime(df[col]).dt.strftime("%d-%m-%Y")
    return df

def calculations(df: pd.DataFrame, calculations: dict = {}):
    """
    Metrics and calculations
    Args:
        df -> Pandas DataFrame
        calculations -> Dictionary with new column and definition.
    Usage: You can run calculations that involve multiple columns in pandas.
    Example: 'margen': 'precio_venta - costo_vehiculo' 
    Return:
        df -> Pandas DataFrame with transformed columns.
    """
    for col_name, calculation in calculations.items():
        df[col_name] = df.eval(f"{calculation}")
    return df