# Evil Wizard

```sql
<?php
  include "./config.php";
  login_chk();
  $db = dbconnect();
  if(preg_match('/|_|\.|proc|union|sleep|benchmark/i', $_GET[order])) exit("No Hack ~_~");
  $query = "select id,email,score from prob_evil_wizard where 1 order by {$_GET[order]}"; // same with hell_fire? really?
  echo "<table border=1><tr><th>id</th><th>email</th><th>score</th>";
  $rows = mysqli_query($db,$query);
  while(($result = mysqli_fetch_array($rows))){
    if($result['id'] == "admin") $result['email'] = "**************";
    echo "<tr><td>{$result[id]}</td><td>{$result[email]}</td><td>{$result[score]}</td></tr>";
  }
  echo "</table><hr>query : <strong>{$query}</strong><hr>";

  $_GET[email] = addslashes($_GET[email]);
  $query = "select email from prob_evil_wizard where id='admin' and email='{$_GET[email]}'";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if(($result['email']) && ($result['email'] === $_GET['email'])) solve("evil_wizard");
  highlight_file(__FILE__);
?>
```

Only thing that is different from hellfire is the stuff under preg_match, So the same script from hellfire works here.
