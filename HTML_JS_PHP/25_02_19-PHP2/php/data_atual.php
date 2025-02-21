<?php
setlocale(LC_TIME, 'pt_BR.UTF-8');
date_default_timezone_set('America/Campo_Grande');

$data = strftime('%A, %d de %B de %Y', strtotime('today'));
echo ucfirst($data);
?>
