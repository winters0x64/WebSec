```php
<?php
  include "./config.php";
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\./i', $_GET['id'])) exit("No Hack ~_~");
  if(strlen($_GET['id']) > 7) exit("too long string");
  $no = is_numeric($_GET['no']) ? $_GET['no'] : 1;
  $query = "select id from prob_red_dragon where id='{$_GET['id']}' and no={$no}";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if($result['id']) echo "<h2>Hello {$result['id']}</h2>";

  $query = "select no from prob_red_dragon where id='admin'"; // if you think challenge got wrong, look column name again.
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if($result['no'] === $_GET['no']) solve("red_dragon");
  highlight_file(__FILE__);
?>
```
So here we are taking an id and a no, the length of id couldn't be more than 7(we can use the CRLF bypass here), then its verifying if no is a number if not it'll be 1 by default.

So We can use the newline trick ie %0a to bypass the length check of id,

So out query is as follows, if we give id as '||no>#&no=%0a our query would be as follows and when we give no as %0a the newline character it will be.

```sql
select id from prob_red_dragon where id=''||no>#' and no=%0a
```
So lets analyze how %0a helps solving the length of id problem, as we could just try to bruteforce the number from id paramter itself but since it can only be 7 characters long, we give %0a as the value for no, that means any input that we give after the %0a will be treated in a new line and and thus we could escape the commented out part coz # is only a single line command in sql, and using newline is a trick to bypass it, after which we can pass in the number which we want to search and just like that through brute forcing we'll get the number.