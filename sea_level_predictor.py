import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot

    fig = plt.figure()

    plt.scatter(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit

    l_reg = linregress(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
    slope = l_reg.slope
    y_intercept = l_reg.intercept

    x_pred = pd.Series([i for i in range(1880, 2051)])
    x_pred
    y_pred = slope*x_pred+y_intercept
    y_pred

    preds = pd.DataFrame(y_pred)
    preds.index = x_pred

    plt.plot(preds, color = "red")

    # Create second line of best fit

    df2 = df.copy()
    df2 = df[(df['Year'] >= 2000)]

    l_reg2 = linregress(x = df2['Year'], y = df2['CSIRO Adjusted Sea Level'])
    slope2 = l_reg2.slope
    y_intercept2 = l_reg2.intercept

    x_pred2 = pd.Series([i for i in range(2000, 2051)])
    x_pred2
    y_pred2 = slope2*x_pred2+y_intercept2
    y_pred2

    preds2 = pd.DataFrame(y_pred2)
    preds2.index = x_pred2

    plt.plot(preds2, color = "green")

    # Add labels and title

    plt.title("Rise in Sea Level")
    plt.ylabel("Sea Level (inches)")
    plt.xlabel("Year")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()