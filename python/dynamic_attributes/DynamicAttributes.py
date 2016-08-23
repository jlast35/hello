#this technique should work for dynamically creating and assigning 1:1 mapped tags

class DynamicClass:
    pass

dc = DynamicClass()
dynamicAttributeString = "dynamicAttribute"
dynamicValue = "dynamicValue"

print dynamicAttributeString, "exists?:", hasattr(dc,dynamicAttributeString)

print "Creating dynamic attribute..."
setattr(dc, dynamicAttributeString, dynamicValue)

print dynamicAttributeString, "exists?:", hasattr(dc,dynamicAttributeString)
print "Value of dynamic attribute:", getattr(dc,dynamicAttributeString)

#TODO: is there a way to handle 1:* tags?

print "Creating an empty list dynamically..."
dynamicList = []
setattr(dc, dynamicAttributeString, dynamicList)
print "Value of dynamic attribute:", getattr(dc, dynamicAttributeString)

print "Appending to the list dynamically..."
#next line makes an assumption - that the attribute returned is a list
getattr(dc, dynamicAttributeString).append(dynamicValue)
print "Value of dynamic attribute:", getattr(dc, dynamicAttributeString)

#apparently, there is...
