<?php
include("conn.php");

$first_name = mysqli_real_escape_string($con, $_POST["first_name"]);
$last_name = mysqli_real_escape_string($con, $_POST["last_name"]);
$fone = mysqli_real_escape_string($con, $_POST["fone"]);
$address = mysqli_real_escape_string($con, $_POST["address"]);
$email = mysqli_real_escape_string($con, $_POST["email"]);
$sexo = mysqli_real_escape_string($con, $_POST["sexo"]);
$tipo_usuario = mysqli_real_escape_string($con, $_POST["tipo_usuario"]); 

$query_insert = "INSERT INTO usuario (nome, lastname, sexo, fone, address, email, senha, setor) 
                VALUES ('$first_name', '$last_name', '$sexo', '$fone', '$address', '$email', '$senha', '$tipo_usuario')";

<?php
if (mysqli_query($con, $query_insert)) {
    echo "<script>alert('Usuário cadastrado com sucesso!');</script>";
    echo "<script>window.location.href = 'admin.php';</script>";
} else {
    echo "<script>alert('Erro ao cadastrar: " . mysqli_error($con) . "');</script>";
}
?>
