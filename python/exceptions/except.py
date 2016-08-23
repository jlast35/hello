import traceback
try:
    print 1/0
except:
    #print sys.exc_info()
    #print sys.exc_info()[0]
     e = traceback.format_exc()
    print e
