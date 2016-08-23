from xlrd import open_workbook,error_text_from_code
book = open_workbook('simple.xlsx')
sheet = book.sheet_by_index(0)
print error_text_from_code[sheet.cell(0,3).value]
