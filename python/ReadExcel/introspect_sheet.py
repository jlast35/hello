from xlrd import open_workbook,cellname

book = open_workbook('simple.xlsx')
sheet = book.sheet_by_index(0)

print "Sheet Name: " + sheet.name,'\t',
print "Rows: " + str(sheet.nrows),'\t',
print "Columns:" + str(sheet.ncols)

for row_index in range(sheet.nrows):
    for col_index in range(sheet.ncols):
        print cellname(row_index,col_index),'-',
        print str(sheet.cell(row_index,col_index).value),'\t',
    print