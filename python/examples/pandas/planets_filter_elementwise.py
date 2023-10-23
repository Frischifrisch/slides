import sys
import pandas as pd

filename = sys.argv[1] if len(sys.argv) == 2 else "planets.csv"
df = pd.read_csv(filename)

selector = (df['Mass'] > 1) & (df['Mass'] < 100)
print(selector)
print()

planets = df[ selector ]
print(planets)
