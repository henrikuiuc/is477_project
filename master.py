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
