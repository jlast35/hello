import re
text = "123\t123456/234567\tFirst Line.\n\t\t\t\tSecond line.\n\t\t\t\tThird line.\n456\t345678/456789\t1st Line.\n\t\t\t\t2nd line.\n\t\t\t\t3rd line.\n789\t445678/456789\t1st Line.\n\t\t\t\t2nd line.\n\t\t\t\t3rd line.\n"

##matches = re.finditer(r"^[^\t]+\t(\d{2})(\d{2})(\d{2})/(\d{2})(\d{2})(\d{2})\t(.+?\n)",text,flags=re.MULTILINE)
##for match in matches:
##    print match.group()
    
text = re.sub(r"(?m)^[^\t]+\t(\d\d)(\d\d)(\d\d)/(\d\d)(\d\d)(\d\d)\t(.+\n)",r"1\n\1:\2:\g<3>0 --> \4:\5:\g<6>0\n\7", text)
text = re.sub(r"(?m)^\t{4}","",text)
text = re.sub(r"(?ms)^(1\n.+?)(?=1\n)",r"\1\n",text)
print text
