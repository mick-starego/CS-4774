import pandas as pd

pd.read_csv("crash_data_raw.csv").sample(frac=.05).to_csv("crash_data_sample.csv")
