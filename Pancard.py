import re 

def Pancard_extractor(file): 
    with open(file,"r") as pan : 
        contents = pan.read()
        pattern = r"(?i)\bPAN(?:\s+NO\.?|\s+NUMBER|\s+CARD)?\s*[:=|]\s*([A-Z]{5}[0-9]{4}[A-Z])\b"
        extract = re.findall(pattern,contents)
    return extract 

if __name__=="__main__":
    result = Pancard_extractor("loan_applications_raw.txt")
    print(result)
    
        