<?php
if (isset($_GET['num1']) && isset($_GET['num2'])) {
    $num1 = $_GET['num1'];
    $num2 = $_GET['num2'];
    
    if (is_numeric($num1) && is_numeric($num2)) {

        $resultadoSoma = $num1 + $num2;
        $resultadoSubtracao = $num1 - $num2;
        $resultadoMultiplicacao = $num1 * $num2;
        $resultadoDivisao = $num2 != 0 ? $num1 / $num2 : 'Divisão por zero não é permitida';

        echo "<p>O resultado da soma é: " . $resultadoSoma . " (Tipo: " . gettype($resultadoSoma) . ")</p>";
        echo "<p>O resultado da subtração é: " . $resultadoSubtracao . " (Tipo: " . gettype($resultadoSubtracao) . ")</p>";
        echo "<p>O resultado da multiplicação é: " . $resultadoMultiplicacao . " (Tipo: " . gettype($resultadoMultiplicacao) . ")</p>";
        echo "<p>O resultado da divisão é: " . $resultadoDivisao . " (Tipo: " . gettype($resultadoDivisao) . ")</p>";
    } else {
        echo "<p>Os valores fornecidos não são números válidos.</p>";
    }
} else {
    echo "<p>Algum dos valores não foi definido.</p>";
}
?>