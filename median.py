import statistics
import pandas as pd

df = pd.read_csv("data.csv")
data = df["Weight(Pounds)"].tolist()

median = statistics.median(data)
print("The median is ", median)