<?php
session_start();

if (!isset($_SESSION['nome']) || !isset($_SESSION['setor'])) {
    header('location: index.html');
    exit();
} 