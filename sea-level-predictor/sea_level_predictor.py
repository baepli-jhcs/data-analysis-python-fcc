import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    best_fit = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x = pd.Series([i for i in range(1880, 2051)])
    y = best_fit.slope * x + best_fit.intercept
    plt.plot(x, y)

    # Create second line of best fit
    df_years = df.loc[df["Year"] >= 2000]
    best_fit = linregress(df_years["Year"], df_years["CSIRO Adjusted Sea Level"])
    x = pd.Series([i for i in range(2000, 2051)])
    y = best_fit.slope * x + best_fit.intercept
    plt.plot(x, y)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()


draw_plot()
