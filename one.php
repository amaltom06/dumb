<?php
$students = array("SOORYA", "AMAL", "ANURAG", "SAFAL","ALAN");
echo "Original Array:\n<br>";
print_r($students);
echo "\n<br> in Ascending Order\n<br>";
asort($students);
print_r($students);
echo "\n<br> in Descending Order\n<br>";
arsort($students);
print_r($students);

?>
