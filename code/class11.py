import pandas

s = pandas.Series([1, 2, 3])
print s

data = {'part': ['fidesz', 'jobbik'], 'szavazat': [60, 40]}
frame = pandas.DataFrame(data)

print frame

df = pandas.read_csv('../data/result_part.csv')
print df.head()

print df[:100]

print df['part']
print df['szavazat']

df['uj'] = 'NaN'

print df.tail()

new = df[df['megye'] == 1][df['telepules'] == 1][df['szavazokor'] == 1]
print df[df.megye == 1][df.telepules == 1][df.szavazokor == 1]
print new

print df.describe()
print df.drop_duplicates()

print df['part'].unique()

print df.groupby('part').mean()
group_megye_part = df['szavazat'].groupby([df['megye'], df['part']])
print group_megye_part.mean()
print group_megye_part.sum()
print group_megye_part.min()
print group_megye_part.median()

print group_megye_part.mean().unstack('part')

osszes_szavazat = df['szavazat'].sum()

group_partok_sum = df['szavazat'].groupby(df['part']).sum()

def calculate_percent(i):
    szazalekos_eredmeny = 100 * i / float(osszes_szavazat)
    return szazalekos_eredmeny

print group_partok_sum.apply(calculate_percent)

group_partok_megye_sum = group_megye_part.sum()

print group_partok_megye_sum.groupby(level=0).apply(calculate_percent)
