<?php
function removeVogais($string) {
    return str_replace(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'], '', $string);
}

if (isset($_GET['texto'])) {
    $texto = htmlspecialchars($_GET['texto']);
    $resultado = removeVogais($texto);
    echo "Texto sem vogais: $resultado";
} else {
    echo "<p>Por favor, insira um texto.</p>";
}
?>
