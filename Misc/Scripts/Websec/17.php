<?php
    function sleep_rand() { /* I wish php5 had random_int() */
        $range = 100000;
        $bytes = (int) (log($range, 2) / 8) + 1;
        do {  /* Side effect: more random cpu cycles wasted ;) */
            $rnd = hexdec(bin2hex(openssl_random_pseudo_bytes($bytes)));
            echo $rnd;
        } while ($rnd >= $range);
        usleep($rnd);
    }

    sleep_rand();
?>