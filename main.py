from . import config

from .data_loading import load_country_data

from .cleaning import clean_datasets

from .comparison import compare_columns

from .plotting import (
    configure_plotting,
    plot_categorical_counts,
    plot_categorical_percentages,
    plot_age_distribution,
    plot_boxplot_by_treatment,
)


def run_analysis():
    """
    Run the complete Mali vs Uganda analysis.
    """

    # -------------------------------------------------------------------------
    # Configure plotting
    # -------------------------------------------------------------------------

    configure_plotting()

    # -------------------------------------------------------------------------
    # Load data
    # -------------------------------------------------------------------------

    mali, uganda = load_country_data(
        mali_file=config.MALI_FILE,
        uganda_file=config.UGANDA_FILE,
        mali_column_mapping=config.COLUMN_MAPPING_MALI,
    )

    # -------------------------------------------------------------------------
    # Compare columns
    # -------------------------------------------------------------------------

    compare_columns(
        mali,
        uganda,
        output_file=config.COLUMN_SIMILARITY_FILE,
    )

    # -------------------------------------------------------------------------
    # Clean data
    # -------------------------------------------------------------------------

    mali, uganda = clean_datasets(
        mali,
        uganda,
        config,
    )

    # -------------------------------------------------------------------------
    # Categorical variables
    # -------------------------------------------------------------------------

    for variable in config.CATEGORICAL_VARS:

        plot_categorical_counts(
            mali,
            uganda,
            variable,
            output_dir=config.OUTPUT_DIR,
        )

    # -------------------------------------------------------------------------
    # Treatment variables
    # -------------------------------------------------------------------------

    for variable in config.TREATMENT_VARS:

        plot_categorical_percentages(
            mali,
            uganda,
            variable,
            output_dir=config.OUTPUT_DIR,
        )

    # -------------------------------------------------------------------------
    # Age distribution
    # -------------------------------------------------------------------------

    plot_age_distribution(
        mali,
        uganda,
        output_dir=config.OUTPUT_DIR,
    )

    # -------------------------------------------------------------------------
    # Haemoglobin
    # -------------------------------------------------------------------------

    plot_boxplot_by_treatment(
        mali,
        uganda,
        outcome_variable="hemoglobin",
        output_dir=config.OUTPUT_DIR,
        title="Hemoglobin by Hydroxyurea Use and Country",
        y_label="Hemoglobin",
        filename="hemoglobin_hydroxyurea_use_mali_vs_uganda.png",
        y_limit=(0, 20),
    )

    # -------------------------------------------------------------------------
    # Mean cell volume
    # -------------------------------------------------------------------------

    plot_boxplot_by_treatment(
        mali,
        uganda,
        outcome_variable="mean_cell_volume",
        output_dir=config.OUTPUT_DIR,
        title="Mean Cell Volume by Hydroxyurea Use and Country",
        y_label="Mean Cell Volume",
        filename="mean_cell_volume_hydroxyurea_use_mali_vs_uganda.png",
        y_limit=(0, 150),
        figsize=(12, 8),
    )


if __name__ == "__main__":
    run_analysis()
