from xlrd import open_workbook

wb = open_workbook('simple.xlsx')

for s in wb.sheets():
    print 'Sheet:',s.name
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(str(s.cell(row,col).value))
        print '\t'.join(values)
    print