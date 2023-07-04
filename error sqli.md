# sqli-labs-write-up
## Error based injections
In this type of injection we have error to help us fuzz the payload, there will be something which reflects our payload on the screen, 
When we keep changing the value of id we get different output’s of username and passwords.. <br>
￼
And by adding  ‘ to id we produce and sql error <br>
￼
So to fix this error we findout the payload that can make the url work…we can understand that the syntax is consist of id=‘’ and the remaining statement.  We comment out the rest of the statement to not give any further error<br>

￼
Now we know the correct paylaod which works so now we can use the union statement the dump the database..<br>
Now we use different sql functions to know about the database <br>
database()- used to find the database name<br>
Version()- we use this to find the  current version of the MySQL database, as a string.<br>
Like ()- we use this functions to find patterns<br>
Here are some examples showing different LIKE operators with '%' and '_' wildcards:<br>
LIKE Operator	Description<br>
WHERE CustomerName LIKE 'a%'	Finds any values that start with "a"<br>
WHERE CustomerName LIKE '%a'	Finds any values that end with "a"<br>
WHERE CustomerName LIKE '%or%'	Finds any values that have "or" in any position<br>
WHERE CustomerName LIKE '_r%'	Finds any values that have "r" in the second position<br>
WHERE CustomerName LIKE 'a_%'	Finds any values that start with "a" and are at least 2 characters in length<br>
WHERE CustomerName LIKE 'a__%'	Finds any values that start with "a" and are at least 3 characters in length<br>
WHERE ContactName LIKE 'a%o'	Finds any values that start with "a" and ends with "o"<br>

Example
SELECT * FROM Customers
WHERE CustomerName LIKE 'a%';


Dual-The dual in sql is used to SELECT a value returned by a function by querying the table. The dual in sql can concatenate two or more strings and return the resultThe dual in sql is used to SELECT a value returned by a function by querying the table. The dual in sql can concatenate two or more strings and return the result…
 
Order by- we use this to find the number of columns in the particular if it exceeds the the value then it show out an error
￼
Union select in mysql :
The UNION operator is used to combine the result-set of two or more SELECT statements.
* Every SELECT statement within UNION must have the same number of columns
* The columns must also have similar data types


Now to use union select we need names of  tables, columns so we use the INFORMATION_SCHEMA provides access to database metadata, information about the MySQL server such as the name of a database or table, the data type of a column. Other terms that are sometimes used for this information are data dictionary and system catalog.

The INFORMATION_SCHEMA.TABLES view allows you to get information about all tables and views within a database. By default it will show you this information for every single table and view that is in the database.<br>
The INFORMATION_SCHEMA.COLUMNS view allows you to get information about all columns for all tables and views within a database. By default it will show you this information for every single table and view that is in the database.<br>
Column name	Data type	Description<br>
TABLE_CATALOG	nvarchar(128)	Table qualifier.<br>
TABLE_SCHEMA	nvarchar(128)	Name of schema that contains the table.<br>
TABLE_NAME	nvarchar(128)	Table name.<br>
COLUMN_NAME	nvarchar(128)	Column name.<br>
The TABLE_SCHEMA function returns the schema name of the object found after any alias chains have been resolved.<br>
￼
Now using all this information lets make a query to <br>
http://localhost:1234/Less-1/?id=-1 'union select 1,2,database()—+<br>
http://localhost:1234/Less-1/?id=-1 'union select 1,2,group_concat(table_name) from information_schema.tables where table_schema=database() limit 0,1—+<br>
http://localhost:1234/Less-1/?id=-1 'union select 1,2,group_concat(column_name) from information_schema.columns where table_name='emails' limit 0,1—+<br>
http://localhost:1234/Less-1/?id=-1'union select 2,group_concat(id),group_concat(email_id) from  emails --+<br>
http://localhost:1234/Less-1/?id=-1'union select 2,group_concat(password),group_concat(username) from users --+ <br>





For level 2 use id= 1 <br>
For level 3  use id=2’)<br>
For level 4  use id =3”)<br>
Lab 11 -> lab 1 but in user input<br>
Lab 12 -> lab 2<br>












