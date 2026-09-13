from pathlib import Path

import seaborn as sns
import matplotlib.pyplot as plt

from .comparison import (
    compare_categories,
    compare_numeric_variable,
)


# =============================================================================
# Plot configuration
# =============================================================================

def configure_plotting():
    """Configure seaborn plotting style."""

    sns.set_theme(
        style="whitegrid",
        context="paper",
        font_scale=0.9,
    )

    sns.set_style(
        "whitegrid",
        {
            "grid.linewidth": 0.5,
            "axes.linewidth": 0.8,
            "axes.edgecolor": "0.3",
        },
    )


def save_plot(filename, output_dir):
    """
    Save the current matplotlib figure.
    """

    output_dir = Path(output_dir)
    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    plt.savefig(
        output_dir / filename,
        dpi=300,
        bbox_inches="tight",
    )


# =============================================================================
# Categorical plots
# =============================================================================

def plot_categorical_counts(
    mali,
    uganda,
    variable,
    output_dir,
    show=True,
):
    """
    Plot category counts for Mali vs Uganda.
    """

    plot_data = compare_categories(
        mali,
        uganda,
        variable,
        statistic="count",
    )

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=plot_data,
        x="Category",
        y="Count",
        hue="Country",
    )

    plt.title(
        f"{variable.replace('_', ' ').title()}: Mali vs Uganda",
        fontsize=13,
        fontweight="normal",
    )

    plt.xlabel("")
    plt.ylabel(
        "Number of participants",
        fontsize=10,
    )

    plt.xticks(
        fontsize=9,
        rotation=45,
        ha="right",
    )

    plt.yticks(fontsize=9)

    plt.legend(
        title="Country",
        frameon=False,
        fontsize=9,
        title_fontsize=9,
    )

    sns.despine()
    plt.tight_layout()

    save_plot(
        f"{variable}_mali_vs_uganda.png",
        output_dir,
    )

    if show:
        plt.show()

    plt.close()


def plot_categorical_percentages(
    mali,
    uganda,
    variable,
    output_dir,
    show=True,
):
    """
    Plot category percentages for Mali vs Uganda.
    """

    plot_data = compare_categories(
        mali,
        uganda,
        variable,
        statistic="percentage",
    )

    plt.figure(figsize=(8, 5))

    sns.barplot(
        data=plot_data,
        x="Category",
        y="Percentage",
        hue="Country",
    )

    plt.title(
        variable.replace("_", " ").title(),
        fontsize=13,
        fontweight="normal",
    )

    plt.xlabel("")
    plt.ylabel("Percentage (%)")
    plt.ylim(0, 100)

    plt.legend(
        title="Country",
        frameon=False,
    )

    sns.despine()
    plt.tight_layout()

    save_plot(
        f"{variable}_mali_vs_uganda.png",
        output_dir,
    )

    if show:
        plt.show()

    plt.close()


# =============================================================================
# Age distribution
# =============================================================================

def plot_age_distribution(
    mali,
    uganda,
    output_dir,
    mali_age_column="age_visit_years",
    uganda_age_column="calculated_age",
    show=True,
):
    """
    Plot age distributions for Mali and Uganda.
    """

    plt.figure(figsize=(8, 5))

    sns.kdeplot(
        mali[mali_age_column].dropna(),
        fill=True,
        alpha=0.3,
        label=f"Mali — {mali_age_column}",
    )

    sns.kdeplot(
        uganda[uganda_age_column].dropna(),
        fill=True,
        alpha=0.3,
        label=f"Uganda — {uganda_age_column}",
    )

    plt.xlabel("Age (years)")
    plt.ylabel("Density")
    plt.title(
        "Age distribution by country",
        fontsize=12,
    )

    plt.legend(
        title="Country / variable"
    )

    sns.despine()
    plt.tight_layout()

    save_plot(
        "age_distribution_mali_vs_uganda.png",
        output_dir,
    )

    if show:
        plt.show()

    plt.close()


# =============================================================================
# Boxplots
# =============================================================================

def plot_boxplot_by_treatment(
    mali,
    uganda,
    outcome_variable,
    output_dir,
    title,
    y_label,
    filename,
    y_limit=None,
    figsize=(10, 8),
    show=True,
):
    """
    Plot a numeric outcome by hydroxyurea use and country.
    """

    plot_data = compare_numeric_variable(
        mali,
        uganda,
        variable=outcome_variable,
        group_variable="using_hydroxyurea",
    )

    plt.figure(figsize=figsize)

    sns.boxplot(
        data=plot_data,
        x="using_hydroxyurea",
        y=outcome_variable,
        hue="Country",
    )

    if y_limit is not None:
        plt.ylim(*y_limit)

    plt.xlabel("Using Hydroxyurea")
    plt.ylabel(y_label)
    plt.title(title)

    sns.despine()
    plt.tight_layout()

    save_plot(
        filename,
        output_dir,
    )

    if show:
        plt.show()

    plt.close()
