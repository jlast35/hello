import xml.etree.ElementTree as ET
tree = ET.parse('menu.mml')
root = tree.getroot()
print ET.tostring(root)
#for node in root: print node

#from xml.dom import minidom
#xmldoc = minidom.parse('menu3.mml')
#print xmldoc.toxml()
