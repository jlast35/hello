import re
text = "<t>text</t>"
match = re.search(r"(<[^/]*?>)(.*)",text)
print match.group(2)