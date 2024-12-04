<?php
$nome = $_POST['nome'];
$rg = $_POST['rg'];
$cpf = $_POST['cpf'];
$endereco = $_POST['end'];
$idade = $_POST['idade'];
$epocas_ano = $_POST['epoca_ano'] ?? [];
$genero = $_POST['genero'];
$cor = $_POST['cor'];
$cartao = $_POST['cartao'];
$botao_fav = $_POST['botao_fav'];
$pokemons = $_POST['pokemon'] ?? [];
$ranger = $_POST['ranger'];
$data = $_POST['data'];

echo "Nome: $nome<br>";
echo "RG: $rg<br>";
echo "CPF: $cpf<br>";
echo "Endereço: $endereco<br>";
echo "Idade: $idade<br>";

echo "Estações do ano favoritas: " . implode(", ", $epocas_ano) . "<br>";

echo "Gênero: $genero<br>";
echo "Cor favorita: $cor<br>";
echo "Número do cartão: $cartao<br>";
echo "Botão favorito: $botao_fav<br>";

echo "Pokémons favoritos: " . implode(", ", $pokemons) . "<br>";

echo "Power Ranger favorito (cor): $ranger<br>";
echo "Data de sua morte: $data<br>";
?>
