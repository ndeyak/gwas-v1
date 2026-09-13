import pandas as pd


def load_csv(file_path, column_mapping=None):
    """
    Load a CSV file and optionally rename its columns.

    Parameters
    ----------
    file_path : str or pathlib.Path
        Path to the CSV file.

    column_mapping : dict, optional
        Mapping from original to standardised column names.

    Returns
    -------
    pandas.DataFrame
    """

    df = pd.read_csv(file_path)

    if column_mapping:
        df = df.rename(columns=column_mapping)

    return df


def load_country_data(
    mali_file,
    uganda_file,
    mali_column_mapping=None,
):
    """
    Load the Mali and Uganda datasets.
    """

    mali = load_csv(
        mali_file,
        column_mapping=mali_column_mapping,
    )

    uganda = load_csv(uganda_file)

    return mali, uganda
