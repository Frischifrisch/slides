import sys
import pandas as pd

filename = sys.argv[1] if len(sys.argv) == 2 else "survey_results_public.csv"
df = pd.read_csv(filename, usecols=['Country', 'OpenSourcer', 'CompTotal'])
print(df.head())

