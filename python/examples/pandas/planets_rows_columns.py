import sys
import pandas as pd

filename = sys.argv[1] if len(sys.argv) == 2 else "planets.csv"
df = pd.read_csv(filename)

small = df[2:5][['Distance (AU)', 'Planet name']]
print(type(small))
print(small)
print()

other = df.iloc[3:6][['Distance (AU)', 'Planet name']]
print(type(other))
print(other)
print()

