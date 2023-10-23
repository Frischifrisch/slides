import sys
import pandas as pd

filename = sys.argv[1] if len(sys.argv) == 2 else "planets.csv"
df = pd.read_csv(filename)

mass = df['Mass'] # Get Series
print(type(mass))
print(mass)
print()

one_col = df[['Mass']] # Get DataFrame
print(type(one_col))
print(one_col)
print()

two_cols = df[['Planet name', 'Mass']] # Select multiple columns, get DataFrame
print(type(two_cols))
print(two_cols)
print()

