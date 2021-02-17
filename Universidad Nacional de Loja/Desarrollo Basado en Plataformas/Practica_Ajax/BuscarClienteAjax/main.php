<!--$host="localhost";
$port=3306;
$socket="";
$user="root";
$password="elvis123";
$dbname="clienteajax";

$con = new mysqli($host, $user, $password, $dbname, $port, $socket)
	or die ('Could not connect to the database server' . mysqli_connect_error());

//$con->close();

-->

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ajax y PHP</title>
</head>

<body>
    <h2>Mis Clientes</h2>
    <select name="select">
        <?php
        $con = @mysqli_connect("localhost", "root", "elvis123", "pruebaajax",3306);
        if (!$con) {
            echo "<p> Error al conectar con la BD " . mysqli_connect_error() . "</p>";
            exit;
        }
        $sentencia = "select * from clientes";
        if (!($resultado = mysqli_query($con, $sentencia))) {
            echo "<p> Error al ejecutar consulta </p>";
        }
        //fetch Obtener una fila de resultado como un array asociativo
        while ($fila = mysqli_fetch_assoc($resultado)) {
            echo "<option value='{$fila['Id']}'>{$fila['Nombre']}</option>";
        }
        mysqli_free_result($resultado);
        mysqli_close($con);
        ?>
    </select>
</body>

</html>