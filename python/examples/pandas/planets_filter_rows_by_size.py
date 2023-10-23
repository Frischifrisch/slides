import sys
import pandas as pd

filename = sys.argv[1] if len(sys.argv) == 2 else "planets.csv"
df = pd.read_csv(filename)


big_ones_selector = df['Mass'] > 1
print(big_ones_selector)
print()

big_ones = df[big_ones_selector]
print(big_ones)
