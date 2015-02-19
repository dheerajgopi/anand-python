import tablib

def csv2xls(csv_file, xls_file):
    csv_2_xls = tablib.Dataset()
    data = open(csv_file)

    for lines in data:
        line = lines.strip()
        val = line.split(',')
        csv_2_xls.append([val[0], val[1]])

    with open(xls_file + '.xls','wb') as f:
        f.write(csv_2_xls.xls)

csv2xls('testcsv.csv', 'abc')
