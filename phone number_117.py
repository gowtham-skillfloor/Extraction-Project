import re
def number_extractor(file):
   with open(file, "r") as fhand:
        contents=fhand.read()
        pattern=r"[6-9]\d{9}"
        extract = re.findall(pattern,contents)
        return extract

if __name__=="__main__":
   result=number_extractor("customer_support_tickets.txt")
   print(result)

