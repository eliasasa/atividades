<!DOCTYPE html>
<html lang="en">
<head>
<!-- Name: Open PHP/HTML/JS In Browser -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script type=text/javascript>
    nome=window.prompt("Nome?");
    </script>
    <?php
    $color = "preto";
    echo "Meu carro é " .$color. "<br>";
    // echo "Minha casa é $color";
    // echo "Minha bicicleta é " .$coLOR. "<br>";
    // const CONSTANTE = 0.0;
    // echo CONSTANTE;
    $nome = $_GET['nome'];
    echo "Nome: $nome";
    ?>
</body>
</html>