import marimo

__generated_with = "0.10.0"
app = marimo.App()

@app.cell
def _():
    import marimo as mo
    return (mo,)

@app.cell
def _():
    import pandas as pd
    df = pd.read_csv("data/features/events.csv")
    df
    return (df,)

@app.cell
def _(df, mo):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.hist(df["duration_minutes"], bins=30, edgecolor="black")
    ax.set_xlabel("Duration (minutes)")
    ax.set_ylabel("Count")
    ax.set_title("Distribution of Event Durations")

    mo.mpl.interactive(fig)
    return (fig, ax)
