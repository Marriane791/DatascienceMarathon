import  re 
phone = "2004-959-559"#this is the phone number
#re.sub(pattern,repl,string,max=0)  
#delete python-style comments
num = re.sub(r'#.*$',"",phone)
print("Phone Num:",num)
#Remove anything other than digits
num = re.sub(r'\D',"",phone)
print("Phone Num:",num)