<?php
if (isset($_POST['nome']) && isset($_POST['idade'])) {
    $nome = htmlspecialchars($_POST['nome']);
    $idade = intval($_POST['idade']);
    
    echo "Olá, $nome! Você tem $idade anos.";
} else {
    echo "Por favor, insira seu nome e idade.";
}
?>
