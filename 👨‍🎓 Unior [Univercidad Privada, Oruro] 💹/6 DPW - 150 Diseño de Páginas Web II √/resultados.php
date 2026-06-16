<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RESULTADOS</title>
</head>
<body>
    <?php
    $conexion=mysqli_connect("localhost", "root", "12345678", "prueba") or die ("Problemas de conecxion");
    $registros=mysqli_query($conexion, "select  codigo, nombre, email, codigopush from estudiantes") 
    or die ("Problemas con los registros").mysql_error($conexion);
    while ($reg=mysqli_fetch_array ($registros))
     {
        echo "Codigo: ".$reg['codigo']."<br>";
        echo "Nombre: ".$reg['nombre']."<br>";
        echo "Email: ".$reg['email']."<br>";
        echo "Codigo: ".$reg['codigopush']."<br>";
        echo "Curso: ";
        switch ($reg['codigopush'])
         {
            case 1:
                echo "PHP";
            break;
            case 2:
                echo "ASP";
            break;
            case 3:
                echo "JSP";
            break;
        }
        echo "<br>";
        echo "<hr>";
        
     }
     mysqli_close($conexion);
    ?>
</body>
</html>