<?php
$leds = [
    "1"=> 2,
    "2"=> 5,
    "3"=> 5,
    "4"=> 4,
    "5"=> 5,
    "6"=> 6,
    "7"=> 3,
    "8"=> 7,
    "9"=> 6,
    "0"=> 6
];

$N = (int)readline("Apareceu?");

$cases = [];
for ($i = 0; $i < $N; $i++){
    $cases[] = readline();
}

foreach($cases as $case){
    $nleds = 0;
    $nums = str_split($case);
    foreach($nums as $num){
        $nleds += $leds[$num];
    }

    echo "$nleds leds\n";
}