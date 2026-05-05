## Crude Oil Volatility and Inflation: A Notable Relationship?
A Repository for IS477 project.

# Contributors
- Henrik Weidemanis
- Andres Bustamente

# Summary
In this project, we have decided to see how strong the correlation between inflation and oil volatility is. The relationship between oil prices and inflation is well established: after all, oil is used in transportation for almost everything, so oil going up brings up the prices for almost everything. However, it is not so clear with volatility, since volatility only describes the magnitude of how much any asset moves, not necessarily which direction it goes.

The initial motivation for this project was drawn from Henrik’s passion for financial derivatives. At the time we selected groups, concerns over the price of oil were high because of geopolitical tensions. We wanted a way to see if the volatility itself, regardless of whether prices actually rose or not, would impact inflation. Though we now know oil prices and inflation are higher, it is still a research question we want to pursue.

To do this, we needed a way to get data for inflation and oil volatility. When researching alternatives for volatility data, we realized that we would need to calculate it ourselves since oil volatility indexes only became popular in the early 2000s. As a workaround, we decided to use widely available oil price data to calculate volatility ourselves. Because we would be working with American inflation data, we chose to calculate our volatility from WTI (West Texas Intermediate), which tracks the price of oil that is sourced within the United States. For inflation data, we will use the consumer price index, or CPI. The CPI tracks the price of a ‘basket’ of goods, and it is calculated and released monthly by the Federal Reserve. Fortunately, both sets of data can be retrieved using the same API, the same one we used for the S&P 500 assignment earlier this semester.

After doing some visualizations showing the relationship between the correlation between our two variables and the amount of “lag” in our volatility data, we realized that volatility has the greatest impact on inflation 3 months after the fact. Because of this, we fit our linear regression later in the project with data that is lagged by 3 months. This introduces 3 null values at the start of the data, which we believe doesn’t have a big impact on the model since the input size is so large.

To implement our research question, we decided the best way to go about it was through a Python script. Both of us are familiar with Python thanks to our work in this class, other classes, and internships, so we thought it would be natural for us to continue with it as our tool. All work that isn’t final is stored on Jupyter notebooks due to easy testing, while the final version of the workflow is stored in a Python file named “master.py” to indicate its special status. In our file, the main library we utilized was Pandas due to its flexibility in data cleaning and merging. We used Matplotlib for outputting graphs (which are returned as PNGs when you run the file in a folder locally), and finally, we used Scikit-learn for a quick linear regression model.

Our findings indicate that there is a weak, but noticeable, relationship between oil volatility and inflation. The relationship is especially noticeable when a 3-month lag is introduced in the volatility data. We believe this is because logistics companies usually purchase fuel ahead of time at set prices, so it takes time for oil price instability to have an effect on the prices of other goods. This is indicated by our linear regression model, which returns this equation: 

Expected Inflation % Month over Month = 2.5% baseline inflation + 1.0284 * monthly oil volatility.

Here, the baseline inflation in a way where 1% is written as 1, while volatility is passed into the model as decimals (30% volatility is 0.3).

# Data Profile

# Data Quality

# Data Cleaning

# Findings

# Future Work

# Challenges

# Reproducing (steps)

# References (FRED Citations)
