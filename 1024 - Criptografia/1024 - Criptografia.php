<?php
$n = (int) readline();
for ($i = 0; $i < $n; $i++) {
    $text = readline();
    $chars = str_split($text);
    //Primeira Passada
    for ($j = 0; $j < count($chars); $j++) {
        $char = $chars[$j];
        $ascii = ord($char);
        if (isChar($ascii)) {
            $chars[$j] = chr($ascii + 3);
        }
    }

    //Segunda Passada
    $chars = array_reverse($chars);

    //Terceira Passada
    $middle = (int) (count($chars) / 2);
    for ($j = $middle; $j < count($chars); $j++) {
        $char = $chars[$j];
        $ascii = ord($char);
        $chars[$j] = chr($ascii - 1);
    }
    $text = implode($chars);
    echo $text . "\n";
}

function isChar(int $asciiChar)
{
    return ($asciiChar >= 65 && $asciiChar <= 90) || ($asciiChar >= 97 && $asciiChar <= 122);
}
