<?php
if (isset($_GET['idade'])) {
    $idade = intval($_GET['idade']);
    
    if ($idade >= 60) {
        echo "<p>Idoso.</p>";
    } elseif ($idade >= 18) {
        echo "<p>Maior de idade.</p>";
    } elseif ($idade >= 0) {
        echo "<p>Menor de idade.</p>";
    } else {
        echo "<p>Valor inválido.</p>";
    }
} else {
    echo "<p>Valor inválido.</p>";
}
?>
