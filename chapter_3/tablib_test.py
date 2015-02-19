import tablib

data = tablib.Dataset()

data.append(['A', 1])
data.append(['B',2])

with open('testcsv.csv', 'wb') as f:
    f.write(data.csv)

with open('testxls.xls', 'wb') as f:
    f.write(data.xls)
