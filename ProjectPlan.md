Overview:
Throughout the course of the project, we want to answer a financial question relating to commodity markets. Specifically, we want to see how volatility in oil prices (not prices themselves) relates to the rate of inflation. We will do this by seeing how oil volatility, which we will calculate, mathematically correlates with inflation. We will use scipy cross-correlation as our metric. This project is inspired by the recent rapid shifts in the price of oil.

To answer our question, we will first identify a source for oil data. For the purpose of this project, we will focus on the American economy, so our oil price data will come from historical data on West Texas Intermediate oil prices. For inflation data, we will use CPI, or consumer price index. CPI tracks the change in price of a ‘basket’ of different goods. Fortunately, both of these items are easily found through FRED (Federal Reserve Bank St. Louis), and they can be loaded into Python with the same API we’ve used for class.

Once the data is loaded in, we will assess the data’s quality and perform data cleaning to prepare the data for analysis. Once the data is ready, we will calculate the volatility of oil prices from the price data using this equation. From that, we will compare the volatility of oil to inflation values to see how they’re related.

Team:
Team members Henrik Weidemanis and Andres Bustamente will have equal responsibility in completing project work. For sections requiring contextualization of economic data, Henrik will be responsible as his background is in finance.

Research and business questions (Henrik)
Simply put, we want to see how oil volatility correlates with inflation. Inherently, this question is backward-looking and analytical. However, we believe that the relationship between volatility and inflation can be useful in a business context. For example, a view on inflation is crucial when valuing stocks and bonds.

Datasets (Andres)
All data from St. Louis fed (WTI and CPI, can be downloaded as CSV or pinged with API)

U.S. Energy Information Administration, Crude Oil Prices: West Texas Intermediate (WTI) - Cushing, Oklahoma [DCOILWTICO], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DCOILWTICO, March 8, 2026.

Organization for Economic Co-operation and Development, Consumer Price Index: All Items: Total for United States [CPALTT01USM657N], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/CPALTT01USM657N, March 8, 2026.

Timeline
Before gathering our data, the first step we will take is writing a short background document to accompany the data. We will assume that readers of our work will be familiar with basic economic concepts, but we want to ensure that all readers are able to make the most of our work. This background document will be useful when it comes time to write the final report.
Next, we will get the data loaded into Python via either manual download or the FRED API. As of right now we are leaning towards manual download, as we want to ensure that our API keys are kept private. To ensure that results are reproducible, we will specify a date range that we sample from (which is especially important given recent moves in oil prices).
Once the data is loaded in, we will need to calculate volatility. The only input for this calculation is price, so the price data from WTI is sufficient. Since volatility is a measure for a given period, we will have the "volatility window" match the frequency of inflation data. With volatility and inflation data having the same frequency, our data analysis will be easier.
With data ready, we will be able to conduct our analysis by comparing 2 time-series (volatility and inflation) to see their correlation.


Constraints: There are some constraints we should keep in mind that could affect our analysis. First, this is a daily series, but it only includes prices on trading days when the market is actually open. This means the timeline will have gaps on weekends and holidays, which can complicate time series analysis if we expect perfectly consecutive dates. We will need to decide whether to fill the missing values, interpolate them, or just work around them.

Another consideration is that these prices are nominal, meaning they have not been adjusted for inflation. When doing any kind of long-term trend analysis spanning multiple years, the raw numbers might be misleading because a dollar in 2010 does not have the same purchasing power as a dollar today. So we need to keep in mind that context matters in these cases.

The data also represents spot prices in a specific place. While WTI is a global benchmark, these are not future prices and do not directly reflect what traders are paying for contracts down the line. If we want to forecast or understand market expectations, we might actually need future curve data. Additionally, the series is not seasonally adjusted, which means any regular seasonal patterns in oil demand and pricing remain in the data, potentially masking or distorting other signalsif we are not accounting for them.

We should also be aware that extreme events can create outliers that look like data errors but are actually real market phenomena. 

Gaps (Henrik)




