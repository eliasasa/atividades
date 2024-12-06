<?php

$host = "localhost";
$usuario = "root";
$senha = "";
$bd = "teste_php";
 
$con = new mysqli($host, $usuario, $senha, $bd);
 
if($con -> connect_errno){
    echo "Falha na Conexão: (".$con -> connect_errno.")" .$con -> connect_error;
}
 
else{
    echo $con->host_info."<br>Tudo certo<br>";
}