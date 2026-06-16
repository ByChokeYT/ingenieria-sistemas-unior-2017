<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Documento sin título</title>
</head>

<body>
<?php
$a1=$_POST["a1"]; 
$a2=$_POST["a2"]; 
$a3=$_POST["a3"]; 
$suma=$a1+$a2+$a3; 
echo "suma".$suma;
/*Nótese como, en las próximas líneas se incluyen "if" dentro de otros "if" (anidación) */
if ($suma!=180) { // comienza la llave "1" 
        // El signo != significa "distinto de".
    echo "<p>Los ángulos ingresados no corresponden a un triángulo</p>"; 
} else { //fin 1, comienzo 2 
    if ($a1==$a2 && $a2==$a3) { // comienzo 3.  
        /* "&&" implica que ambas condiciones deben cumplirse para que se ejecuten las acciones por verdadero. */
        echo "<p>El triángulo es equilátero</p>"; 
    } else { // fin 3, comienzo 4 
                   if ($a1==$a2 || $a2==$a3 || $a1==$a3) { 
                       // comienzo 5.  
                       /*Para que se evalúe como falso, todas las condiciones deben ser falsas. Caso contrario, es verdadero. */
                echo "<p>El triángulo es isósceles</p>"; 
        } else { //fin 5, comienzo 6 
                echo "<p>El triángulo es escaleno</p>"; 
            } //fin 6 
        } //fin 4 
    } //fin 2 
?>
</body>
</html>