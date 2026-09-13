import pandas as pd


def compare_columns(
    mali,
    uganda,
    output_file=None,
):
    """
    Compare columns present in the Mali and Uganda datasets.

    Returns
    -------
    pandas.DataFrame
        Side-by-side column listing.
    """

    mali_columns = list(mali.columns)
    uganda_columns = list(uganda.columns)

    print(f"Mali has {len(mali_columns)} columns")
    print(f"Uganda has {len(uganda_columns)} columns")

    column_df = pd.DataFrame({
        "Mali": pd.Series(mali_columns),
        "Uganda": pd.Series(uganda_columns),
    })

    if output_file is not None:
        column_df.to_excel(
            output_file,
            index=False,
        )

    return column_df


def category_counts(df, variable, country):
    """
    Calculate category counts for one country.
    """

    result = (
        df[variable]
        .fillna("Missing")
        .value_counts()
        .rename("Count")
        .reset_index()
    )

    result.columns = [
        "Category",
        "Count",
    ]

    result["Country"] = country

    return result


def category_percentages(df, variable, country):
    """
    Calculate category percentages for one country.
    """

    result = (
        df[variable]
        .fillna("Missing")
        .value_counts(normalize=True)
        .mul(100)
        .rename("Percentage")
        .reset_index()
    )

    result.columns = [
        "Category",
        "Percentage",
    ]

    result["Country"] = country

    return result


def compare_categories(
    mali,
    uganda,
    variable,
    statistic="count",
):
    """
    Create comparison data for a categorical variable.

    Parameters
    ----------
    statistic : {"count", "percentage"}
        Statistic to calculate.
    """

    if statistic == "count":

        mali_data = category_counts(
            mali,
            variable,
            "Mali",
        )

        uganda_data = category_counts(
            uganda,
            variable,
            "Uganda",
        )

    elif statistic == "percentage":

        mali_data = category_percentages(
            mali,
            variable,
            "Mali",
        )

        uganda_data = category_percentages(
            uganda,
            variable,
            "Uganda",
        )

    else:
        raise ValueError(
            "statistic must be 'count' or 'percentage'"
        )

    return pd.concat(
        [mali_data, uganda_data],
        ignore_index=True,
    )


def compare_numeric_variable(
    mali,
    uganda,
    variable,
    group_variable=None,
):
    """
    Combine numeric data from Mali and Uganda.

    Optionally includes a grouping variable such as
    using_hydroxyurea.
    """

    columns = [variable]

    if group_variable is not None:
        columns.insert(0, group_variable)

    mali_data = mali[columns].copy()
    mali_data["Country"] = "Mali"

    uganda_data = uganda[columns].copy()
    uganda_data["Country"] = "Uganda"

    return pd.concat(
        [mali_data, uganda_data],
        ignore_index=True,
    )
