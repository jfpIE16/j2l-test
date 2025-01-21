import argparse
import logging

import json
import pandas as pd

from utils.db import DatabaseConnection
from consts import SCHEMA, NAME_CHANGE, CALCULATIONS, DB_SCHEMA
from transforms import string_normalization, coalesce_cols, change_column_name, handle_blanks, format_date, calculations

def extract(filepath) -> pd.DataFrame:
    logging.info(f"Extracting data from {filepath}")
    return pd.read_json(filepath)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    transfomed_df = (
        df.pipe(string_normalization, schema=SCHEMA)
        .pipe(coalesce_cols)
        .pipe(change_column_name, schema_change=NAME_CHANGE)
        .pipe(handle_blanks, schema=SCHEMA)
        .pipe(format_date, schema=SCHEMA)
        .pipe(calculations, calculations=CALCULATIONS)
    )
    logging.info("Transforming vehicle data.")
    return transfomed_df

def load(df: pd.DataFrame) -> bool:
    con = DatabaseConnection()
    with con.get_connection() as connection:
        rowcount = df.to_sql('vehiculos', con=connection, dtype=DB_SCHEMA, index=False, if_exists='replace')
        logging.info(f"Succesfully loaded {rowcount} rows.")


def run(args):
    filepath = args.filepath
    df_extract = extract(filepath)
    df_transformed = transform(df_extract)
    load(df_transformed)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--filepath',
        default='data/test_tecnico.json',
        type=str,
        help='Indicate file to load.'
    )
    parser.add_argument(
        '-log',
        '--loglevel',
        default='warning',
        help=(
            'Provide logging level. Example --loglevel, debug, default=warning'
        )
    )

    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel.upper())
    run(args)