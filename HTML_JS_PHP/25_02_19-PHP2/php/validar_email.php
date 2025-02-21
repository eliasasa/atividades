<?php
function validaEmail($email) {
    if (filter_var($email, FILTER_VALIDATE_EMAIL) && strpos($email, '@') && strpos($email, '.')) {
        return "E-mail válido.";
    } else {
        return "E-mail inválido.";
    }
}

if (isset($_GET['email'])) {
    $email = htmlspecialchars($_GET['email']);
    $resultado = validaEmail($email);
    echo $resultado;
} else {
    echo "<p>Por favor, insira um e-mail.</p>";
}
?>
