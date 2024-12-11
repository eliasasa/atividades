<?php 
        include("verificacao.php");
        if($_SESSION["setor"]!="adm"){
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
    <form method="post" action="action_user.php">

    Nome <br><input type="text" name="first_name" id="fn"><br>

    Sobrenome <br><input type="text" name="last_name" id="In"><br>

    Fone <br><input type="text" name="fone" id="fone"><br>

    Endereço <br><input type="text" name="address" id="add"><br>

    Email<br> <input type="text" name="email" id="email"><br>
    Sexo:<br>
    <input type="radio" name="sexo" id="masculino" value="Masculino"> Masculino<br>
    <input type="radio" name="sexo" id="feminino" value="Feminino"> Feminino<br>
    <input type="radio" name="sexo" id="outro" value="Outro"> Outro<br>

    Tipo de Usuário: <br>
    <input type="radio" name="tipo_usuario" id="adm" value="adm" required> Administrador<br>
    <input type="radio" name="tipo_usuario" id="comum" value="comum"> Usuário Comum<br>
    
    <button type="submit">Enviar</button>
    </form>
    <a href="logout.php">Sair</a>
</body>
</html>