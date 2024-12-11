<?php 
        include("verificacao.php");
        if($_SESSION["setor"]!="comum"){
            header("location:index.html");
            exit();
        }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>
        USER
    </p>
    <a href="logout.php">Sair</a>
</body>
</html>