from xlrd import open_workbook,empty_cell

print empty_cell.value

book = open_workbook('simple.xlsx')
sheet = book.sheet_by_index(0)
empty = sheet.cell(1,3)
blank = sheet.cell(2,3)
print empty is blank, empty is empty_cell, blank is empty_cell

#book = open_workbook('simple.xlsx',formatting_info=True) #sadly, formatting_info=True will only work with xls not xlsx
#sheet = book.sheet_by_index(0)
#empty = sheet.cell(1,3)
#blank = sheet.cell(2,3)
#print empty.ctype,repr(empty.value)
#print blank.ctype,repr(blank.value)