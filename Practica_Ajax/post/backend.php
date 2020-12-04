<?php
$con = @mysqli_connect("localhost", "root", "elvis123", "pruebaajax",3306);
if (!$con) {
    echo "<p> Error al conectar la base de datos" . mysqli_connect_error() . "</p>";
    exit;
}

$sentencia = "select * from clientes where Id='$_GET[id]'";
if (!($resultado = mysqli_query($con, $sentencia))) {
    echo "<p>Error al ejecutar la consulta</p>";
}

while ($fila = mysqli_fetch_assoc($resultado)) {
    echo "{$fila['Descripcion']}";
}
mysqli_free_result($resultado);
mysqli_close($con);
?>