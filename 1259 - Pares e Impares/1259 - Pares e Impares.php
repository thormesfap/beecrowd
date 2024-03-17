<?php

$N = (int) readline();
$pares = [];
$impares = [];
$count = 0;
while($count < $N){
    $number = (int) readline();
    if($number % 2 == 0){
        $pares[] = $number;
    } else{
        $impares[] = $number;
    }
    $count++;
}
sort($pares);
rsort($impares);
for($i = 0; $i < count($pares); $i++){
    echo $pares[$i] . "\n";
}
for($i = 0; $i < count($impares); $i++){
    echo $impares[$i] . "\n";
}