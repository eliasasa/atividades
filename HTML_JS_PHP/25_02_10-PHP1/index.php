<?php

$nome = 'João Oliveira';
$meunome = 'Elias'; 
$endereco = 'Morro do macaco';
$idade = 19;
$curso = 'ads';
$cidade = 'Campo Grande';
$estado = 'MS';
$banda = 'Rammstein';


echo '<style>
body {
    background-color: black;
    color: white;
</style>';

echo "<h1>Seu nome é $nome, ele tem " . mb_strlen(str_replace(' ', '', $nome)) . " caracteres</h1><br>";
echo "<h1>Olá $meunome" . " seu novo endereço: $endereco". " foi registrado no sistema!</h1>";

echo "<h1> Meu nome é $meunome, tenho $idade anos, curso $curso, moro em $cidade - $estado e estou escutando $banda<h1>";

$nota1 = 4; $nota2 = 10; $media = ($nota1 + $nota2)/2;
echo "<h2>Sua média é $media</h2>";

$preco = 140; $desconto = $preco * 0.1; 
echo "<h2>Valor do produto: $preco<br>Com desconto de 10% do PIX: ". ($preco - $desconto). "</h2>";

$idadeLC = 26; $idadeAna = 16; $idadeDavi = 18; $idadeJoao = 25; $idadeRafael = 20;
$mediaidade = ($idadeAna + $idadeDavi + $idadeJoao + $idadeLC + $idadeRafael)/5;
echo "<h2>A média de idade dos meus inimigos é $mediaidade";

?>
