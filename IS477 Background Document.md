IS477 Background Document

This document will serve as a way for readers with a non-finance background to get familiar with the goal of our project and the data we are using.
Our primary goal is to see how oil volatility relates to inflation. 
Inflation is the process of the prices of goods and services rising. Inflation can happen for many reasons, the most explicit being more money being printed. 
Volatility is simply how volatile the price of an underlying asset is. Volatility is not prices moving in any specific direction. For example, a stock that moves 10% every day is very volatile, but it may not actually move anywhere if it alternates between up and down days.
Volatility is a well tracked metric within finance, with companies like CBOE publishing the OVX Index to track specifically oil volatility. Unfortunately OVX only goes back to 2010, and we want more data than that, so we will have to calculate volatility ourselves. 
Volatility as a metric describes a period of time. Because we want to capture sharp price movements, we will calculate volatility using a rolling window of 20 days, and then average out daily volatility calculations over a span of months so that we can more easily compare it to inflation data.
Inflation data will come from the CPI, or consumer price index. The CPI is a metric calculated by the federal reserve that tracks the price of a "basket" of goods. CPI is released monthly and covers data from the previous month. 
It is well established that rising prices and inflation are correlated. We seek to learn if volatility, and the uncertainty coming from it, is also correlated to inflation.