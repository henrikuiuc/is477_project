# This is the master file for the whole project. This file is intended to run the entire project workflow, with the only necessary external file being an API key.
# As such, the file must be ran in the same folder as a .txt with a FRED API key, which can be acquired for free. 

import pandas as pd
import requests
import numpy as np
from datetime import datetime
import hashlib
import json
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# Data import from API function
def fetch_fred_series(series_id, api_key, observation_start=None, observation_end=None):
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": api_key,
        "file_type": "json",
    }
    if observation_start is not None:
        params["observation_start"] = observation_start.strftime("%Y-%m-%d")
    if observation_end is not None:
        params["observation_end"] = observation_end.strftime("%Y-%m-%d")

    response = requests.get(url, params=params)
    response.raise_for_status()
    observations = response.json()["observations"]

    df = pd.DataFrame(observations)[["date", "value"]]
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")  # "." -> NaN
    return df


# Hashing helper function
def hash_series(df):
    payload = df.sort_values("date").to_json(orient="records", date_format="iso")
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()



# Loading in the data from the API, given that API_KEY.txt is a file that contains a valid key. Obviously, the API key will need to be provided from outside the lab downlaod.
with open("API_KEY.txt", "r") as f:
    FRED_API_KEY = f.read().strip()

start = datetime(1980, 1, 1)
end = datetime(2023, 3, 1)




oil_data = fetch_fred_series("DCOILWTICO", FRED_API_KEY,start,end)
cpi_data = fetch_fred_series("CPIAUCSL", FRED_API_KEY,start,end)



# Loading in cached hash values from the intial lab to see if all is good
with open("data_hashes.json", "r") as f:
    expected_hashes = json.load(f)

# Storing hashes we got from the data imported
current_hashes = {
    "oil": hash_series(oil_data),
    "cpi": hash_series(cpi_data),
}

# Comparing hashes from current data and the cached correct values to check for any discrepancies
for name, current in current_hashes.items():
    if current != expected_hashes[name]:
        raise ValueError(
            f"Hash mismatch for {name}: data has changed since last validated run. "
            f"Expected {expected_hashes[name][:12]}..., got {current[:12]}..."
        )
    if current == expected_hashes[name]:
        print(f'{name} hash looks good!')



# Preparing data for analysis by dropping null values

oil_data = oil_data.dropna(subset=["value"])


# Data frame of monthly volatility for oil.
monthly_vol = (
    oil_data
    .set_index("date")["log_return"]
    .groupby(pd.Grouper(freq="ME"))
    .std()
    .mul(np.sqrt(252)) #sqrt here is for annualized volatility
    .rename("oil_vol_annualized")
    .to_frame()
)

# Data frame of month over month inflation changes
cpi_monthly = (
    cpi_data
    .sort_values("date")
    .set_index("date")["value"]
    .resample("ME")
    .last()
    .rename("cpi")
    .to_frame()
)

# Annualizing the monthly CPI change, just like volatility
cpi_monthly["cpi_mom_annualized"] = (
    (1 + cpi_monthly["cpi"].pct_change()) ** 12 - 1
) * 100



# Merging data sets for comparison on the month and dropping null values
merged_data = monthly_vol.join(cpi_monthly, how="inner").dropna()

# Plotting month over month CPI changes and monthly volatility

fig, ax1 = plt.subplots(figsize=(12, 5))

# Left axis: oil volatility
ax1.plot(merged_data.index, merged_data["oil_vol_annualized"], color="tab:blue", label="Oil vol (annualized)")
ax1.set_xlabel("Date")
ax1.set_ylabel("Annualized oil volatility", color="tab:blue")
ax1.tick_params(axis="y", labelcolor="tab:blue")

# Right axis: CPI MoM annualized
ax2 = ax1.twinx()
ax2.plot(merged_data.index, merged_data["cpi_mom_annualized"], color="tab:red", label="CPI MoM (annualized, %)")
ax2.set_ylabel("CPI MoM annualized (%)", color="tab:red")
ax2.tick_params(axis="y", labelcolor="tab:red")

plt.title("Oil Volatility vs. CPI Month-over-Month (Annualized)")
fig.tight_layout()
plt.savefig("oil_vol_and_monthly_cpi.png")

print('Oil and CPI graph saved to disk!')

# This chart shows that oil volatility appears to precede, which lines up with the idea that volatility and high oil prices are correlated


# This matrix shows that in the same month, oil volatility and month over month inflation are weakly negatively correlated. Not what we expected, but perhaps there is a lag in the relationship?
print(merged_data[["oil_vol_annualized", "cpi_mom_annualized"]].corr())



# We are going to shift the data a bit and see what the correlation values end up being

lags = range(1, 13)  # oil vol leading CPI by up to 12 months, and vice versa
results = []

for k in lags:
    shifted = merged_data["oil_vol_annualized"].shift(k)
    r = shifted.corr(merged_data["cpi_mom_annualized"])
    results.append({"lag": k, "corr": r})

lag_corr = pd.DataFrame(results)

plt.figure(figsize=(8, 4))
plt.bar(lag_corr["lag"], lag_corr["corr"])
plt.axvline(0, color="black", linewidth=0.5)
plt.axhline(0, color="black", linewidth=0.5)
plt.xlabel("Lag (months) — positive = oil vol leads CPI")
plt.ylabel("Correlation")
plt.title("Cross-correlation: oil vol vs CPI MoM")
plt.savefig("lag_and_correlation.png")

print('Lagged volatility and CPI graph saved to disk!')


# Doing a linear regression with the 3 month lagged data, since that is where correlation appears strongest

# Create the 3-month lagged oil vol column
merged_data["oil_vol_lag3"] = merged_data["oil_vol_annualized"].shift(3)

# Drop rows where the lag introduces NaN (the first 3 months)
regression_data = merged_data[["cpi_mom_annualized", "oil_vol_lag3"]].dropna()

X = regression_data[["oil_vol_lag3"]]   
y = regression_data["cpi_mom_annualized"]

model = LinearRegression().fit(X, y)


print('The following data is the intercept and slope of a linear regression model trained on the lagged oil volatility \nand month over month CPI changes.')
print(f"Intercept: {model.intercept_:.4f}")
print(f"Slope:     {model.coef_[0]:.4f}")

print('With lag incorporated, we can see that oil volatility and inflation are positively, but weakly correlated.\n This is done through a simply implemented linear regression, and the positive coeficient assigned to the 3 month lagged volatility variable.')
print('For more information, see the README.md for this GitHub repository.')

