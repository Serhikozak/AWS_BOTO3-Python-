import pandas as pd

df = pd.read_csv('/Users/army/Military/users.csv')

df.drop(df[ df['email'].str.contains('bridge')].index, inplace = True)
print(df)



#s3://skozakov/users.csv
