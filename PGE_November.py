
# coding: utf-8

from lxml import objectify
import pandas as pd

path = '/home/steve/Downloads/PGE_June_Nov.xml'
xml = objectify.parse(open(path))
root = xml.getroot()
for i in root.getchildren():
    print i.getchildren()
intervals = root.getchildren()[7].getchildren()[2].getchildren()
intervals = intervals[0]
intint = intervals.getiterator()
readings = []
for i in intint:
    readings.append(i)
readings2 = []
for i in readings:
    readings2.append(str(i))

readingsf = [int(i) for i in readings2 if len(i) > 0]


hour = []
reads = []
for i in xrange(len(readingsf)):
    if readingsf[i] == 3600:
        hour.append(readingsf[i + 1])
        reads.append(readingsf[i + 2])

df = pd.DataFrame({'HOUR':hour, 'USE':reads})

df['HOUR'] = pd.to_datetime(df['HOUR'],unit='s')

print df.USE.max(), df.USE.min(), df.USE.mean()

df['hourofday'] = [t.hour for t in df.HOUR]
df['dayofweek'] = [t.dayofweek for t in df.HOUR]

df = df.rename(columns={'HOUR': 'Timestamp', 'USE': 'Wh'})
df.to_pickle('/home/steve/Documents/pgexml_june_nov15')

#grouped = df.groupby('hourofday')
