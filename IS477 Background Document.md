## IS477 Background Document


# Purpose
This document will serve as a way for readers with a non-finance background to get familiar with the goal of our project and the data we are using.
Our primary goal is to see how oil volatility relates to inflation. 

# Definitions

Inflation is the process of the prices of goods and services rising. Inflation can happen for many reasons, the most common being an increase in the money supply (money being printed) and the price of input goods going up (like oil). Periods with lower inflation are known as disinflation. Periods with negative inflation, where prices shrink, are known as deflation.


Volatility is simply how volatile the price of an underlying asset is. Volatility is not prices moving in any specific direction. For example, a stock that moves 10% every day is very volatile, but it may not actually move anywhere if it alternates between up and down days. Volatility is traditionally calculated using the daily log return of an asset, then averaging it over the desired time frame. Volatility is a well-tracked metric within finance, with companies like CBOE publishing the OVX Index to track specifically oil volatility. Unfortunately, OVX only goes back to 2010, and we want more data than that, so we will have to calculate volatility ourselves. When calculating volatility, we will find the monthly volatility number. That way, it is easily compared to monthly inflation metrics released by the Federal Reserve.

Inflation data will come from the CPI, or consumer price index. The CPI is a metric calculated by the Federal Reserve that tracks the price of a "basket" of goods. CPI is released monthly and covers data from the previous month. 

# Goal
It is well established that rising oil prices and inflation are correlated. We seek to determine whether volatility and the uncertainty it creates are also correlated with inflation.
