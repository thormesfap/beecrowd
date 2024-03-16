<?php

while(true){
    [$M, $N] = explode(" ",readline(), 2);
    $M = (int) $M;
    $N = (int) $N;
    if($M <= 0 || $N <= 0){
        break;
    }
    $a = $M < $N ? $M : $N;
    $b = $N < $M ? $M : $N;
    $soma =  0;
    while($a <= $b){
        echo $a . " ";
        $soma += $a;
        $a++;
    }
    echo "Sum=$soma\n";
}
