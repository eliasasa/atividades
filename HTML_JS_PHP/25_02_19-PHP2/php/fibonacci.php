<?php

$resultados = [1];
$numAnterior = 1;
$numAtual = 1;

for ($i = 2; $i <= 10; $i++) {
    $proximoNum = $numAnterior + $numAtual;
    $numAnterior = $numAtual;
    $numAtual = $proximoNum;
    $resultados[] = $numAtual;
}

echo "Primeiros 10 valores de Fibonacci: ";
foreach ($resultados as $valor) {
    echo "<p>$valor</p><br>";
}

?>
