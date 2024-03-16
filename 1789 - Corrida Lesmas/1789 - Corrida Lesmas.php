<?php

while($qt = (int) readline()){
    $lesmas  = explode(" ", readline(), $qt);
    $lesmas = array_map(fn ($lesma) => (int) $lesma, $lesmas);
    $maior = 0;
    for($i = 0; $i < $qt; $i++){
        if($lesmas[$i] > $maior){
            $maior = $lesmas[$i];
        }
    }
    if($maior < 10){
        echo 1 . "\n";
    } else if($maior < 20) {
        echo 2 . "\n";
    } else{
        echo 3 . "\n";
    }
}

