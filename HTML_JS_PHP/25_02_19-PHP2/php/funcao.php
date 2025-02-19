<?php

if (isset($_GET['largura']) && isset($_GET['comprimento'])) {
    $largura = floatval($_GET['largura']);
    $comprimento = floatval($_GET['comprimento']);
    $area = $largura * $comprimento;

    echo "<script>
        window.alert('Sua área é: $area');
        window.history.back();
    </script>";
} else {
    echo "<p>Valores inválidos.</p>";
}

?>
