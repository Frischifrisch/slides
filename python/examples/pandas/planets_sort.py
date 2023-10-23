import sys
import pandas as pd

filename = sys.argv[1] if len(sys.argv) == 2 else "planets.csv"
df = pd.read_csv(filename)

sorted_df = df.sort_values('Planet name', ascending=True)
print(sorted_df)
# df remains unchanged
