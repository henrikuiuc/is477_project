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
We used two main datasets in this project, both pulled from the Federal Reserve Economic Data API.

Crude Oil Prices (WTI)
This dataset contains the daily spot price of WTI crude oil, measured in USD per barrel. The data goes back to january 1986, but we started our analysis in January 1990 to align with cleaner CPI data. We chose WTI specifically because it is the primary US benchmark for oil prices, which made sense since we were using US inflation data. The raw data includes dates with no trading (weekdays, holidays) which show up as missing values. We kept those in during the fetch stage and handled them during cleaning.

Consumer Price Index for All Urban Consumers
This is a monthly series that tracks the average change in prices paid by urban consumers for a basket of goods and services. It is the most common measure of inflation in the US. The data is seasonally adjusted, which saved us from having to do that ourselves. Values are reported as an index number, so we had to convert it into month-over-month percentage changes to make it interpretable alongside votality.

Both dataset were accessed using the same FRED API endpoint. We stored the raw API response as dataframes with data and value columns. For reproducibility, we hashed each dataset after import and compared against known good hashes

Ethical and legal constraints: FRED data is freely available for academic and personal use. The API key we used is tied to a free FRED acount, and we have excluded our actual key from the public repo. No personally identifiable information or sensitive data is involved, so there are no privacy concerns.

# Data Quality

# Data Cleaning

# Findings

# Future Work

# Challenges

# Reproducing (steps)

# References (FRED Citations)
