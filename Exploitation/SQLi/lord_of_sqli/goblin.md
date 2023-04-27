# goblin

```sql
select id from prob_goblin where id='guest' and no={$_GET[no]}
```

Here first we have to get id='admin' somehow so we have to negate the statement having id=guest so we put no=0 as there would no table where id is guest and no is 0 so the entire statment negates and we get a false statement and then we can do something like this ```-1 OR 1=1 limit 1,1 --+``` as it dumps everything since we can't use single qoutes we have to use limit to get to the admin id.

