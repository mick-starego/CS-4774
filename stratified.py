import pandas as pd
from sklearn.utils import shuffle

df = pd.read_csv("crash_data_raw.csv")
only_K_df = df[df["CRASH_SEVERITY"] == "K"]
other_df = df[df["CRASH_SEVERITY"] != "K"].sample(6000)
combined_df = pd.concat([only_K_df, other_df])
combined_df = shuffle(combined_df)

combined_df.to_csv("crash_data_stratified.csv", index=False)