<?php

$valor = (int)(readline());
$total = $valor;
$notas = [100, 50, 20, 10, 5, 2, 1];
$result = [];
foreach($notas as $nota){
    $qt = (int) ($valor / $nota);
    $result[$nota] = $qt;
    $valor = $valor % $nota;
}

echo $total . "\n";
foreach($result as $key => $value){
    echo "$value nota(s) de R$ " . number_format($key, 2, ",", ".") . "\n";
}