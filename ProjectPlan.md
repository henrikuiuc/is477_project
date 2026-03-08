Overview:
Throughout the course of the project, we want to answer a financial question relating to commodity markets. Specifically, we want to see how volatility in oil prices (not prices themselves) relates to the rate of inflation. We will do this by seeing how oil volatility, which we will calculate, mathematically correlates with inflation. We will use scipy cross-correlation as our metric. This project is inspired by the recent rapid shifts in the price of oil.

To answer our question, we will first identify a source for oil data. For the purpose of this project, we will focus on the American economy, so our oil price data will come from historical data on West Texas Intermediate oil prices. For inflation data, we will use CPI, or consumer price index. CPI tracks the change in price of a ‘basket’ of different goods. Fortunately, both of these items are easily found through FRED (Federal Reserve Bank St. Louis), and they can be loaded into Python with the same API we’ve used for class.

Once the data is loaded in, we will assess the data’s quality and perform data cleaning to prepare the data for analysis. Once the data is ready, we will calculate the volatility of oil prices from the price data using this equation. From that, we will compare the volatility of oil to inflation values to see how they’re related.

Team:
Team members Henrik Weidemanis and Andres Bustamente will have equal responsibility in completing project work. For sections requiring contextualization of economic data, Henrik will be responsible as his background is in finance.

Research and business questions (Henrik)
Simply put, we want to see if how oil volatility correlates with inflation. Inherently, this question is backward looking and analytical. However, we believe that the relationship between volatility and inflation can be useful in a business context. For example, a view on inflation is crucial when valuing stocks and bonds.

Datasets (Andres)
All data from St. Louis fed (WTI and CPI, can be downloaded as CSV or pinged with API)



Timeline
Before gathering our data, the first 



Constraints (Andres)



Gaps (Henrik)
