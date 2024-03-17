<?php

function mdc($a, $b){
    while($b != 0){
        $temp = $a % $b;
        $a = $b;
        $b = $temp;
    }
    return $a;
}

$N = (int) readline();
for($i = 0; $i <$N; $i++){
    [$a, $b] = array_map(fn($n) => (int) $n, explode(" ", readline()));
    echo mdc($a, $b) . "\n";
}