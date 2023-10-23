import sys
import pandas as pd

filename = sys.argv[1] if len(sys.argv) == 2 else "survey_results_public.csv"
size = 10000

for df_chunk in pd.read_csv(filename, chunksize=size):
    print(df_chunk.head())
