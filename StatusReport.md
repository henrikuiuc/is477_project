IS477 Milestone 3: Interim Status Report
Henrik Weidemanis, Andres Bustamante

For this project, we used two datasets from the FRED website (the Federal Reserve Economic Data). We want to see if there is any relationship between oil prices and inflation, so we picked crude oil prices and the consumer price index (CPI) for the US.

The first dataset is called Crude Oil Prices: West Texas Intermediate. This data tracks the price of oil in dollars per barrel. It comes from the US Energy Information Administration. The oil prices in this data go from about $55 to $124 per barrel.

The second dataset is the Consumer Price Index for the US. This comes from the OECD (Organization for Economic Cooperation and Development). CPI basically measures inflation, how much prices go up for regular stuff like food and housing. This data shows percentage changes from month to month. From the stats, CPI goes from negative 1.9% (that is deflation, when prices actually drop) up to positive 1.8% (inflation). The average is around 0.3%.

We picked these two datasets because it is very talked about the fact that when oil prices go up, everything gets more expensive. Like gas, shipping, manufacturing, and everything that uses oil. So higher oil costs might cause higher inflation. We wanted to test if that is true with volatility as well, where prices move violently but not necessarily in any given direction.

One of the problems we noticed is that the oil data has 56 missing values. I think maybe on some days they just did not record the price. We filled those values using the average of the other values. The CPI data had no missing values. We also renamed the columns because the original names were a bit too long, which was not conventional. 

Update to team responsibilities:
Andres' main responsibility will be performing data-quality assessments and connecting data through code so that it can be used later for analysis. This includes the pipeline that is currently on the GitHub repository.
