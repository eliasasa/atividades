<?php
session_start();
if(!$_SESSION['nome']){
    header('location: index.html');
    exit();
}
 