import sys
import pandas as pd

filename = sys.argv[1] if len(sys.argv) == 2 else "planets.csv"
df = pd.read_csv(filename)
print(df)

print()
print(type(df))
print(df.__class__.__name__)
