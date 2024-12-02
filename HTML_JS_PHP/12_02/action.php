<?php
    $nome = $_POST['nome'];
    $genero = $_POST['genero'];
    $ling = $_POST['ling'];
    echo "O nome digitado foi: $nome <br>";
    echo "O gênero escolhido foi: $genero <br>";
    echo "Linguagens escohidas:<br>";
    // for ($i = 0; $i < count($ling); $i++) {
    //     echo "$ling[$i]<br>";
    // };
    foreach($ling as $name) {
        echo "$name<br>";
    }
?>