import pandas as pd
from sklearn.utils import shuffle

df = pd.read_csv("crash_data_raw.csv")
df = df[df["AREA_TYPE"] == "Rural"]
df = df[df["SENIOR_NOTSENIOR"] == "Yes"]

only_K_df = df[df["CRASH_SEVERITY"] == "K"]
other_df = df[df["CRASH_SEVERITY"] != "K"]

print("Num Killed: " + str(len(only_K_df)))
print("Num not killed: " + str(len(other_df)))

if len(only_K_df) > len(other_df):
    only_K_df = only_K_df.sample(len(other_df))
else:
    other_df = other_df.sample(len(only_K_df))

combined_df = pd.concat([only_K_df, other_df])
combined_df = shuffle(combined_df)

combined_df.to_csv("rural_old_stratified.csv", index=False)