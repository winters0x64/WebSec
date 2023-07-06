<?php
/* parse_str(parse_url("http://websec.fr/level25/index.php?page[0]=ok&page[1]=flag&send=Submit")['query'],$query);

foreach ($query as $k => $v) {
    if (stripos($v, 'flag') !== false)
        die('You are not allowed to get the flag, sorry :/');
    } */
    $test = "This is great";
    if((stripos($test,"flag") === false)){
        echo "Ok this worked";
    };
    var_dump(
        parse_url('http://example.com/#@google.com/')
    );
?>