import sys
import pandas as pd

filename = sys.argv[1] if len(sys.argv) == 2 else "planets.csv"
df = pd.read_csv(filename)
print(df)
print()

print(df.loc[3:6])   # by values (here we start from the row where the index column == 3
print()

print(df.iloc[3:6])  # by index (here we start from the 3rd row)
print()

sorted_df = df.sort_values('Planet name', ascending=True)
print(sorted_df)
print()

print(sorted_df.loc[3:6])
print()

print(sorted_df.iloc[3:6])
print()

print('-------')

print(sorted_df.loc[2:4])
print()

print(sorted_df.iloc[2:4])
print()


