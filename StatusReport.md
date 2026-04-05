IS477 Milestone 3: Interim Status Report
Henrik Weidemanis, Andres Bustamante

----

Update on data pipeline work:

For this project, we used two datasets from the FRED website (the Federal Reserve Economic Data). We want to see if there is any relationship between oil prices and inflation, so we picked crude oil prices and the consumer price index (CPI) for the US.
The first dataset is called Crude Oil Prices: West Texas Intermediate. This data tracks the price of oil in dollars per barrel. It comes from the US Energy Information Administration. The oil prices in this data go from about $55 to $124 per barrel.
The second dataset is the Consumer Price Index for the US. This comes from the OECD (Organization for Economic Cooperation and Development). CPI basically measures inflation, how much prices go up for regular stuff like food and housing. This data shows percentage changes from month to month. From the stats, CPI goes from negative 1.9% (that is deflation, when prices actually drop) up to positive 1.8% (inflation). The average is around 0.3%.
We picked these two datasets because it is a very talked-about fact that when oil prices go up, everything gets more expensive. Like gas, shipping, manufacturing, and everything that uses oil. So higher oil costs might cause higher inflation. We wanted to test if that is true with volatility as well, where prices move violently but not necessarily in any given direction.
One of the problems we noticed is that the oil data has 56 missing values. I think maybe on some days they just did not record the price. We filled those values using the average of the other values. The CPI data had no missing values. We also renamed the columns because the original names were a bit too long, which was not conventional. 

----

Update on background document work:

Because this project is very related to finance work, we decided to write a document that describes the data the project concerns and what the goal of the project is. As of completing this status report, the background document first draft has been written. The document includes information about inflation and volatility, which are the two metrics we seek to compare in this project. We hope that with the information available, the project will be more useful to someone who doesn't have a background in business, economics, or finance.

While the first draft is completed, one thing we want to add before the project is completed is a view of historical situations and explanations. For example, we want to add an explainer for oil volatility in the late 70s/early 80s, how that translated into inflation, and what the long term effects of the oil shock were. Not only will this give a real-world case where volatility and inflation are important, but it will also provide readers with a view of why establishing a relationship between volatility and inflation is important.

----

Changes to the project plan:
So far, we have made no changes to the project plan that change our overall vision. We have created updates here to address the comments we got on our original plan. We are committed to using the two data sets we have selected and the tasks we want to do. We have completed the first versions of our background document and data pipeline by the time this document is completed.

Update to team responsibilities:
Andres' main responsibility will be performing data-quality assessments and connecting data through code so that it can be used later for analysis. This includes the pipeline that is currently on the GitHub repository.
Henrik will be responsible for writing the background document and performing the volatility calculation. The background document will provide readers with a chance to familiarize themselves with the terminology being discussed in the project. The volatility calculation will be the main metric we will be comparing with inflation, which is calculated from price data.
Over the course of the project, Andres and Henrik will edit each other's work to ensure that the project vision is consistent.

Update to project timeline:

4/5: 1st version of data pipeline and background document completed
4/12: Background document finalized
4/19: Data pipeline finalized and volatility calculation code written
4/26: Machine learning tools (SkLearn) used to compare volatility and inflation
4/27 - 5/5: Write final report and perform edits where necessary

----

Status of tasks:

Completed: First drafts of pipeline and background document

In progress: Final drafts of pipeline and background document, will be completed by 4/12 and 4/19

Not yet started: Volatility calculation, machine learning script for volatility/CPI comparison, will be completed by 4/26

----

Challenges:

So far, we have not come upon any major challenges. One challenge we foresee is selecting a method to calculate volatility. In particular, we need to select a time frame for the volatility calculation that balances clarity and minimizes the impact of extreme outliers.

