import numpy as np
import pandas as pd


def clean_gender(df, mapping):
    """
    Standardise gender categories.
    """

    if "gender" not in df.columns:
        return df

    df["gender"] = df["gender"].replace(mapping)

    return df


def clean_column(df, column, mapping):
    """
    Apply a replacement mapping to a column if it exists.
    """

    if column in df.columns:
        df[column] = df[column].replace(mapping)

    return df


def clean_mali(df, config):
    """
    Apply Mali-specific cleaning.
    """

    df = clean_gender(
        df,
        config.GENDER_MAPPING,
    )

    df = clean_column(
        df,
        "marital_status",
        config.MALI_MARITAL_STATUS_MAPPING,
    )

    /*
    df = clean_column(
        df,
        "using_hydroxyurea",
        config.MALI_OUINON_MAPPING,
    )*/
    
    for col in config.TREATMENT_VARS:
    	df = clean_column(
        	df,
        	col,
        	config.MALI_OUINON_MAPPING,
    )

    return df


def clean_uganda(df, config):
    """
    Apply Uganda-specific cleaning.
    """

    df = clean_gender(
        df,
        config.GENDER_MAPPING,
    )

    if "hospital_name" in df.columns:
        df["hospital_name"] = (
            df["hospital_name"]
            .astype("string")
            .str.strip()
            .replace(config.UGANDA_HOSPITAL_MAPPING)
        )

    return df


def convert_numeric_columns(df, columns):
    """
    Convert specified columns to numeric values.

    Invalid values are converted to NaN.
    """

    for column in columns:

        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce",
            )

    return df


def clean_datasets(mali, uganda, config):
    """
    Apply all cleaning operations to both datasets.
    """

    mali = clean_mali(mali, config)
    uganda = clean_uganda(uganda, config)

    mali = convert_numeric_columns(
        mali,
        config.MALI_NUMERIC_VARS,
    )

    uganda = convert_numeric_columns(
        uganda,
        config.UGANDA_NUMERIC_VARS,
    )

    return mali, uganda
