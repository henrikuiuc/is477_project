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
This dataset contains the daily spot price of WTI crude oil, measured in USD per barrel. The data goes back to January 1986, but we started our analysis in January 1990 to align with cleaner CPI data. We chose WTI specifically because it is the primary US benchmark for oil prices, which made sense since we were using US inflation data. The raw data includes dates with no trading (weekdays, holidays), which show up as missing values. We kept those in during the fetch stage and handled them during cleaning.

Consumer Price Index for All Urban Consumers
This is a monthly series that tracks the average change in prices paid by urban consumers for a basket of goods and services. It is the most common measure of inflation in the US. The data is seasonally adjusted, which saved us from having to do that ourselves. Values are reported as an index number, so we had to convert it into month-over-month percentage changes to make it interpretable alongside votality.

Both datasets were accessed using the same FRED API endpoint. We stored the raw API response as dataframes with data and value columns. For reproducibility, we hashed each dataset after import and compared against known good hashes

Ethical and legal constraints: FRED data is freely available for academic and personal use. The API key we used is tied to a free FRED account, and we have excluded our actual key from the public repo. No personally identifiable information or sensitive data is involved, so there are no privacy concerns.

# Data Quality
We took data quality seriously because if the raw data changed without us knowing, our results would not be reproducible. The main quality check we implemented was SHA265 hashing.

Here is how it works: after fetching the oil and CPI data from the FRED API, we sort each dataframe by date, convert it to a JSON string in a consistent format, and run that string through SHA256 to generate a fixed-length hash. That hash acts like a fingerprint for the dataset. We then compare that fingerprint to a stored value inside data_hashes.json, which contains the correct hashes from when we first validated the data.

If the hashes match, the script prints a confirmation and proceeds. If they do not match, the script raises a value error and stops immediately. This prevents us from accidentally running analysis on data that has been revised, corrected, or corrupted.

Why would data change? The FRED API occasionally revises historical series; CPI, in particular, gets adjusted when the Bureau of Labor Statistics releases new seasonal factors. Without hashing, we might run the same code a month later and get slightly different results without realizing it. Hashing makes that mismatch explicit.

We chose SHA256 because it is widely used, collision-resistant, and fast enough for datasets of this size. The hash check adds negligible runtime, maybe 0.1 seconds total.

One limitation we acknowledge: hashing only catches changes to the data, not whether the data was already wrong at the time we generated the reference hashes. We manually verified the reference data by spot-checking values against FRED's website before locking in the hashes. We also confirmed that there were no obvious outliers or impossible values.

No other formal data quality checks were implemented, though in retrospect, we could have added checks for things like "CPI should never drop by more than 5% in a single month outside of extreme deflationary periods".

# Data Cleaning
The raw data from FRED was not analysis-ready, so we performed several cleaning operations. 

Oil price data has missing values on days with no trading. We removed any row where the price was missing. This is safe because we later resample to a monthly frequency; losing individual daily prices does not harm our monthly volatility calculation as long as there is enough data within each month. Without this step, calculations like log returns would produce NaNs that cascade through the whole pipeline.

We also computed daily log returns, then we grouped by calendar month, took the standard deviation of daily log returns within each month, and annualized by multiplying by the square root of 252 (the typical number of trading days in a year). Months with very few trading days could produce less stable volatility estimates, but given our multi-decade timespan, this effect averages out.

CPI is released monthly, but the FRED API provides it with a date at the beginning of the month. To align with our monthly volatility data, we resampled CPI. This picks the CPI value reported for that month and attaches it to the month-end date, making the merge clean.

raw CPI is an index, not a return. We computed the month-over-month percentage change, then annualized it, multiplied by 100 to express it as a percentage. This puts inflation on a similar scale to annualized volatility, making comparisons and regressions more interpretable.

When we joined the monthly volatility and the monthly CPI on the date, some months had volatility but no CPI due to slight date mismatches in the resampling step. dropna() after the join removed those rows. We also dropped rows after shifting oil volatility by 3 months for the regression, which introduced NaNs at the start of the series, which we explicitly removed before fitting the model. The loss of three months out of several hundred is negligible.

No imputation or interpolation was used. We preferred to lose a small amount of data rather than introduce assumptions.

# Findings
Our main finding is that oil volatility has a weak positive correlation with inflation, but only when we allow a lag of about three months. In the same month, the correlation was actually slightly negative, which initially confused us. After testing lags from 1 to 12 months, we found the strongest positive correlation at a 3-month lag, with a correlation coefficient around.

We then fit a linear regression using 3-month-lagged oil volatility to predict month-over-month CPI change.

During the 2008 financial crisis, oil volatility spiked dramatically in late 2008. Three months later, in early 2009, CPI month-over-month showed elevated readings despite oil prices having already fallen. Similarly, in early 2020, COVID caused massive oil price swings; by summer 2020, inflation began picking up. These case studies align with our statistical findings. 

We visualize this relationship in two plots. One is a time series overlay showing oil volatility and CPI. You can visually see volatility spikes preceding inflation bumps. The other one is a bar chart of correlation coefficients for lags 1 through 12, with a clear peak at lag 3.

# Future Work
Right now, we have done some basic work. But a quant trader might ask: can lagged oil volatility predict inflation well enough to trade inflation-linked assets? We could construct a simple long/short signal: if 3-month-lagged oil volatility is above a threshold, go long inflation protection. Then backtest that strategy over 1990-2023 to see if it beats a buy-and-hold benchmark. We suspect the signal-to-noise ratio is too low to be profitable after transaction costs, but it is worth testing.

Also, inflation is famously hard to predict. We could improve our model by adding more variables (while keeping others): Lagged inflation, interest rates, supply chain, and exchange rates.

Even a simple multiple linear regression with 2-5 predictors would likely have a much higher R-squared than our current univariate model. From there, we can test whether oil volatility adds incremental predictive power beyond other variables.

We calculated volatility from historical oil prices. But options-implied volatility captures market expectations of future volatility. That's a different economic concept, expected risk vs realized volatility or uncertainty in the options market. The challenge: OVX data only goes back to 2007, so the sample would be much shorter.

Also, the relationship might not be linear. Very high volatility could trigger different inflation dynamics than moderate volatility. A simple check would be to add a squared term to the regression and see if it improves the fit.

# Challenges
Early on, we were not sure whether to lag oil volatility behind inflation or ahead of it. The economic story is that volatility should precede inflation.

We wanted to ensure data integrity, but we argued for a while about where in the pipeline to compute the hashes. We settled on hashing the raw, unmodified dataframes immediately after fetching from the API. That way, the hash checks that the source data has not changed, not our transformed version. If we hashed after cleaning, a change in our cleaning code would break that hash even if the raw data was identical. This seems obvious in hindsight, but at the time, it took us a few messy commits to figure out.

The daily oil price data has missing values for weekends and holidays. When we first calculated log returns, pandas happily shifted prices across missing dates, which produced incorrect returns. We fixed this by ensuring the data was in a regular time index before calculating returns.

# Reproducing (steps)

To reproduce our work, you only need a few files from our repository to get the same results we did. To make the process as simple as possible to follow, we will provide a list of steps to reproduce our results.

1. Create a folder on your computer to hold the necessary files. The title isn’t important, but it may be useful to title it something relating to volatility.
2. Go to the FRED website to get your API key:
2a. If you already have a key, skip to step 4
3. Create an account, then in the top right click on your profile, then API keys. Request an API key and fill out the form.
4. Inside the folder you created, create a text file called “API_KEY.txt” and copy in your key from FRED on the first line.
5. From GitHub, download “data_hashes.json” and “master.py” and put them inside your folder. The JSON is vital for the SHA256 hash check, and master.py is the entire workflow.
6. In a terminal or cmd line, open the folder as your directory and run master.py. The format for Windows is python master.py.
7. Once the workflow runs, it will return two pngs in your folders, which are the visualizations. The terminal will also show a printed statement about the linear regression model.
8. All done!


# References 

U.S. Energy Information Administration, Crude Oil Prices: West Texas Intermediate (WTI) - Cushing, Oklahoma [DCOILWTICO], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DCOILWTICO, May 5, 2026. 

U.S. Bureau of Labor Statistics, Consumer Price Index for All Urban Consumers: All Items in U.S. City Average [CPIAUCSL], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/CPIAUCSL, May 5, 2026. 
