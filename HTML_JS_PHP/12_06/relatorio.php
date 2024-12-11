<?php
include("conn.php");
// include("verificacao.php");
 
$query = "select * from produtos;";
$result = mysqli_query($con, $query);
// $retorno = mysqli_fetch_array($result);
 
// echo $retorno["id_produto"];
// echo $retorno["nome"];
// echo $retorno["descricao"];
// echo $retorno["preco"];
?>
 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório</title>
    <link rel="stylesheet" href="./style.css">
</head>
<body>
    <table border='1'>
    <thead>
        <tr>
            <th>Id</th>
            <th>Nome</th>
            <th>Descrição</th>
            <th>Valor</th>
        </tr>
    </thead>
        <?php
            while($retorno = mysqli_fetch_array($result)){ ?>
                <tr>
                    <td><?php echo$retorno["id_produto"];?></td>
                    <td><?php echo$retorno["nome"];?></td>
                    <td><?php echo$retorno["descricao"];?></td>
                    <td><?php echo$retorno["preco"];?></td>
                </tr>
        <?php } ?> 
    </table>
</body>
</html>
 
