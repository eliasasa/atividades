<?php
 
session_start();
include("conn.php");
 
$nome = mysqli_real_escape_string($con, $_POST["nome"]); //mysqli_real_escape_string evita sql injection
$senha = mysqli_real_escape_string($con, $_POST["senha"]);
 
if (empty($nome) || empty($senha)) {
 
    echo "<script>
            alert('Por favor, preencha todos os campos.');
            window.location.href = 'index.html';
            setTimeout(function(){
                window.location.href = 'index.html';
            }, 2000); // Espera 2 segundos antes de redirecionar
          </script>";
    exit();
}
 
$query = "select * from usuario where nome = '{$nome}' and senha = '{$senha}' ";
 
$result= mysqli_query($con, $query);
 
$row = mysqli_num_rows($result);

$retorno = mysqli_fetch_array($result);
 
// echo $row;
 
if ($row > 0) {
    $_SESSION["nome"] = $nome;
    $_SESSION["setor"] = $retorno['setor'];
    if ($_SESSION["setor"] == 'adm') {
        header("location:admin.php");
        exit();
    } else if ($_SESSION["setor"] == 'comum') {
        header("location:user.php");
        exit();
    }
} else {
    echo "<script>
            alert('Usuário Inexistente.');
            window.location.href = 'index.html';
          </script>";
    exit();
}
 
 
 
 