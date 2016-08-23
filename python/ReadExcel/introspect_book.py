from xlrd import open_workbook

book = open_workbook('simple.xlsx')

print book.nsheets
print
#iterate through sheets by number
for sheet_index in range(book.nsheets):
    print book.sheet_by_index(sheet_index)
print

print book.sheet_names()
print
#iterate through sheets by number
for sheet_name in book.sheet_names():
    print book.sheet_by_name(sheet_name)
print

#iterate through sheets
for sheet in book.sheets():
    print sheet
    for row in [sheet.row(x) for x in range(sheet.nrows)]:
        for cell in row:
            print cell.ctype,
        print