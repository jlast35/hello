from xlrd import open_workbook
import re

wb = open_workbook('CTR_ana_2014-10_eng.xls')

for s in wb.sheets():
    print 'Sheet:',s.name

    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            try:
                value = unicode(s.cell(row,col).value)
                value = re.sub(r"\n","",value)
                #value = unicode(s.cell_type(row,col))+value
                values.append(value)
            except UnicodeEncodeError:
                print "********************Exception Caught****************************************"
                print type((s.cell(row,col).value))
        #print '\t'.join(values)
    #print