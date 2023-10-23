import sys
import pandas as pd

filename = sys.argv[1] if len(sys.argv) == 2 else "planets.csv"
df = pd.read_csv(filename)

print(df.columns)
print()

print(df.dtypes)
print()

print(df.index)
print()

print(df.values)
print()

print(df.describe())

