# orc

```sql 
select id from prob_orc where id='admin' and pw='{$_GET[pw]}'
```
This one is easy to bypass but we need to bypass the following by ?pw=' or 1=1 --+

```sql
$_GET[pw] = addslashes($_GET[pw]); 
$query = "select pw from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
$result = @mysqli_fetch_array(mysqli_query($db,$query)); 
if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orc"); 
```

As i imagined it's a blind sqli attack so would have to write a script(Present in Scripts folder).