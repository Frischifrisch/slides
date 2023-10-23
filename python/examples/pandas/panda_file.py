import sys
import pandas as pd

filename = sys.argv[1] if len(sys.argv) == 2 else "survey_results_public.csv"
country_name = 'Israel'
chunks = []
dev_chunks=[]
for chunk in pd.read_csv(filename, usecols=['Country','DevType'],chunksize=10000):
    part = chunk[chunk['Country'] == country_name]

#df = pd.read_csv(filename, usecols=['Country','DevType'])
#,chunksize=10000):
#for chunk in pd.read_csv(filename, usecols=['Country','DevType'],chunksize=10000):
#    part = chunk[chunk['Country'] == country_name]
#
#
#    print(chunk.size)
#    print(part.size)
#    print('--')
    chunks.append(part)
#
#
df = pd.concat(chunks)
print(df.dtypes)
for value in ['Academic researcher','Data or business analyst', 'Data scientist or machine learning specialist','Database administrator','Designer', 'Developer, back-end',
              'Developer, desktop or enterprise applications','Developer, embedded applications or devices','Developer, front-end','Developer, full-stack','Developer, game or graphics', 'Developer, mobile','Developer, QA or test',
              'DevOps specialist','Educator','Engineer, data', 'Engineer, site reliability','Engineering manager', 'Marketing or sales professional', 'Product manager', 'Scientist',
              'Senior Executive (C-Suite, VP, etc.)', 'System administrator']:
#for value in ['Academic researcher','Data or business analyst', 'Designer']:
    print(value)
    #df[value]= df.apply(lambda row: 1, axis=1)
    #df[value]= df.apply(lambda row: value in str(row['DevType']), axis=1)
    df[value]= df.apply(lambda row: pd.notnull(row['DevType']) and value in row['DevType'], axis=1)

print(df.count())
print(df.size)
print(df)


