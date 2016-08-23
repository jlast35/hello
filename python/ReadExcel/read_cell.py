from xlrd import open_workbook,XL_CELL_TEXT

book = open_workbook('simple.xlsx')
sheet = book.sheet_by_index(0)

cell = sheet.cell(0,0)

print "Cell contents: ",cell
print "Cell Value: ",cell.value
print "Cell is text?: ",cell.ctype==XL_CELL_TEXT

for i in range(sheet.ncols):
    print "Cell type: ",sheet.cell_type(1,i)," \tCell Value: ", sheet.cell_value(1,i)