<?php
parse_str(parse_url("http://websec.fr/level25/index.php?campaignid=%campaignid%&adid=%bannerid%")['query'],$query);
$url = "_search?q=sku:89399";

//var_dump($query);
var_dump(parse_url($url));


foreach ($query as $k => $v) {
    $test = "This is great";
    if (stripos($v, 'flag') !== false)
        die('You are not allowed to get the flag, sorry :/');
    }

?>