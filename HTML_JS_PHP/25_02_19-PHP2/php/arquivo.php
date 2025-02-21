<?php
$arquivo = 'notas.txt';

$conteudo = file_get_contents($arquivo);
echo nl2br($conteudo);

$adicional = "\nFinal do conteúdo";
file_put_contents($arquivo, $adicional, FILE_APPEND);
?>
