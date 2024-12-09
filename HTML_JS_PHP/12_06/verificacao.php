<?php
session_start();

if (!isset($_SESSION['nome']) || !isset($_SESSION['setor'])) {
    header('location: index.html');
    exit();
}

if ($_SESSION['setor'] === 'adm') {
    // header('location: admin.php');
} elseif ($_SESSION['setor'] === 'comum') {
    header('location: user.php');
    exit();
} else {
    header('location: index.html');
    exit();
}
