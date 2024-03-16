<?php

$cases= [];
while(true){
    $ipt = readline();
    $lista = explode(" ", $ipt);
    $lista = array_map(fn($input) => (int) $input, $lista);
    if (array_sum($lista) == 0){
        break;
    }
    $cases[]=$lista;
}

foreach($cases as $case){
    [$hi, $mi, $hf, $mf] = $case;

    $horas = $hf - $hi;
    $minutos = $mf - $mi;

    if ($minutos < 0){
        $minutos += 60;
        $horas -= 1;
    }

    if ($horas < 0){
        $horas += 24;
    }

    if($horas == 0 && $minutos == 0){
        $horas = 24;
    }

    echo $horas * 60 + $minutos . "\n";
}