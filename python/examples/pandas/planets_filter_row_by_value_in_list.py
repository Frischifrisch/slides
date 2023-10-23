import sys
import pandas as pd

filename = sys.argv[1] if len(sys.argv) == 2 else "planets.csv"
df = pd.read_csv(filename)


planet_selector = df['Planet name'].isin(['Earth', 'Mars'])
print(planet_selector)
print()

planets = df[ planet_selector ]
print(planets)
