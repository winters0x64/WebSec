```sql
<?php
  include "./config.php";
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\.|proc|union/i', $_GET[order])) exit("No Hack ~_~");
  $query = "select id,email,score from prob_hell_fire where 1 order by {$_GET[order]}";
  echo "<table border=1><tr><th>id</th><th>email</th><th>score</th>";
  $rows = mysqli_query($db,$query);
  while(($result = mysqli_fetch_array($rows))){
    if($result['id'] == "admin") $result['email'] = "**************";
    echo "<tr><td>{$result[id]}</td><td>{$result[email]}</td><td>{$result[score]}</td></tr>";
  }
  echo "</table><hr>query : <strong>{$query}</strong><hr>";

  $_GET[email] = addslashes($_GET[email]);
  $query = "select email from prob_hell_fire where id='admin' and email='{$_GET[email]}'";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if(($result['email']) && ($result['email'] === $_GET['email'])) solve("hell_fire");
  highlight_file(__FILE__);
?>
```

Here we need to get the admin's email. We also have blind sql injection, also we are using SQL CASE statements. if we get the correct guess we are ordering it using its id otherwise we are ordering it by its score value. So when we enter the correct value the first row of the result would be our admin's row.

(If you're confused about how the sql query works in the script at first the case statement goes through all the rows in the table and creates a column with the value that the sql case returns a column with the values then order by orders this row in ascending order... that's how even invalid rows and columns work)