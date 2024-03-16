<?php

$a = (int)readline();
$b = (int)readline();
$lista = [$a, $b];
sort($lista);
[$a, $b] = $lista;
$a++;
while ($a < $b){
    $resto = $a % 5;
    if ($resto == 2 || $resto == 3){
        echo $a . "\n";
    }
    $a++;
}