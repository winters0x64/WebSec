# Bonus levels 24,25a,25b,26,33,36

level 24 -> sqli in the query returned by the database,(pretty basic)

level 25a -> Here OR and AND are filtered out, So we have to pass OR in the url as '||' and AND as '%26%26' why because AND could be represented as && but Since due to url encoding it will && as way to seperate parameters, hence we have to supply the url encoded form AND inorder for it to be interpreted  as a part of the data, this is why we need url encoding.

level 26a -> Similar to lesson 25 here we're filtering out OR,AND but here we're also bypassing spaces well we can bypass this by supplying a payload like this 
100' %a0 union %a0 select %a0 1,2,3 %a0 %26%26 '1 this is just similar to the payload  100' union select 1,2,3 and '1, Which can be seen from the filtered output as follows
100'�union�select�1,database(),3�&&'1,Here the non printable characters are taken as spaces and here %a0 represents that no printable character. Another way to incorporate spaces is as follows  UNION(select (1),(2),(3)) this query yields the same output as union select 1,2,3.

