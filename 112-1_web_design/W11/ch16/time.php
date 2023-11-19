<?php
header('Content-Type: text/event-stream');
header('Cache-Control: no-cache');

$time = date('Y-m-d H:i:s');
echo "data: 伺服器時間: {$time}\n\n";
flush();
?>