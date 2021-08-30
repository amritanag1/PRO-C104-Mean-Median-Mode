import pandas as pd
import statistics 
 
df = pd.read_csv("data.csv")
data = df["Weight(Pounds)"].tolist()

sum = 0

count = 0

for i in data:
    sum = sum + i
    count = count+1

a = sum/count
print("The mean is ",a)