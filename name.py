import re

def name_extractor(file):
    with open(file,'r') as fhand:
        contents = fhand.read()
        pattern = r"(?:Name|name|Customer|cust name|Customer Name|Cust)\s*[:=]\s*([A-Za-z]+ [A-Za-z]+)"
        extract=re.findall(pattern,contents)
        return extract

if __name__=='__main__':
    result=name_extractor("customer_support_tickets.txt")
    print(result)