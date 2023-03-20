<?php
highlight_file(__FILE__);
include 'flag.php';
if (isset($_GET['passwd'])) {

        if (hash("md5", $_GET['passwd']) == '0e514198421367523082276382979135'){
            echo' <html><head><link href="style.css" rel="stylesheet"></head><body>
            
            <div class="flash"style="text-align:center;margin-top:10%">ACCESS GRANTED : '.$flag.'</div></body></html>';
        } else {
            echo'<html><head><link href="style.css" rel="stylesheet"></head><body>
            <div class="flash" style="text-align:center; margin-top:10%">ACCESS DENIED</div></body></html>';
    
    }
}
?>


