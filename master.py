# This is the master file for the whole project. This file is intended to run the entire project workflow, with the only necessary external file being an API key.
# As such, the file must be ran in the same folder as a .txt with a FRED API key, which can be acquired for free. 

import pandas as pd
import requests
import numpy as np
import datetime
import matplotlib.pyplot as plt
