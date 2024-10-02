import pandas as pd
import altair as alt
import sys
import os


def create_plot(df, y_column, title):
    chart = (
        alt.Chart(df)
        .mark_line()
        .encode(
            x="step:Q",
            y=alt.Y(f"{y_column}:Q", scale=alt.Scale(zero=False)),
            color="rev:N",
        )
        .properties(width=600, height=400, title=title)
    )
    return chart


def main(metrics_file):
    # Read the CSV file
    df = pd.read_csv(metrics_file)

    plots = [
        ("train/acc", "Training Accuracy"),
        ("val/acc", "Validation Accuracy"),
        ("train/loss", "Training Loss"),
        ("val/loss", "Validation Loss"),
    ]

    for column, title in plots:
        chart = create_plot(df, column, title)
        output_file = f'{column.replace("/", "_")}_plot.png'
        chart.save(output_file)
        print(f"Generated plot: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_plots.py <path_to_metrics_csv>")
        sys.exit(1)

    metrics_file = sys.argv[1]
    if not os.path.exists(metrics_file):
        print(f"Error: File {metrics_file} does not exist.")
        sys.exit(1)

    main(metrics_file)
