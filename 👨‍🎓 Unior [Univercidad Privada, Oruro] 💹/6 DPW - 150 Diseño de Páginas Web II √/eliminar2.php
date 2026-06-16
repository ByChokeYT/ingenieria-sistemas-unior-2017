<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ELIMINAR REGISTROS</title>
</head>
<body>
    <?php
      $conexion=mysqli_connect("localhost","root","12345678","prueba") or die ("Problemas con la base de datos");
      $registros=mysqli_query($conexion,"select * from estudiantes where email='$_REQUEST[email]'") or die ("Fallo");
      if ($reg=mysqli_fetch_array($registros)) 
      {
        mysqli_query($conexion, "delete from estudiantes where email='$_REQUEST[email]'") or die ("Problemas en el SELECT");
        echo "el alumno fue eliminado exitosamente";
      }
      else
      {
          echo "No existe un alumno con ese email";
      }
      mysqli_close($conexion);
    ?>
</body>
</html>