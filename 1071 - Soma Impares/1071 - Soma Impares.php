<?php

$X = (int) readline();
$Y = (int) readline();

$lista = [$X, $Y];
sort($lista);
[$X, $Y] = $lista;
$soma = 0;
$X++;
while ($X < $Y){
    if(abs($X % 2) > 0){
        $soma += $X;
    }
    $X++;
}
echo $soma . "\n";