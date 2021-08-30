import statistics
import pandas as pd

df = pd.read_csv("data.csv")
data = df["Weight(Pounds)"].tolist()

mode = statistics.mode(data)
print("The mode is", mode)