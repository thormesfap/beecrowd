<?php

$N = (int) readline();
for($i = 0; $i < $N; $i++){
    $text = readline();
    $shift = (int) readline();
    $chars = str_split($text);
    for($j = 0; $j < count($chars); $j++){
        $cod = ord($chars[$j]);
        $order = $cod - 64;
        $new = $order - $shift;
        if($new <= 0){   
            $new = $new + 26;
        }
        $chars[$j] = chr($new + 64);
    }
    $cypher = implode("", $chars);
    echo $cypher . "\n";
}