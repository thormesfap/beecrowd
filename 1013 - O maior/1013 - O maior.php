<?php


function maior(int $a, int $b)
{
    return ($a + $b + abs($a - $b)) / 2;
}

[$n1, $n2, $n3] = explode(" ", readline(), 3);

$maior = maior(maior($n1, $n2), $n3);
echo "$maior eh o maior\n";
