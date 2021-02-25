<?php
    include('coneccionBD.php');
    if(isset($_POST["action"]))  {
	if($_POST["action"] == "insert") {
		$query = "
		INSERT INTO persona (nombre, apellido) VALUES ('".$_POST["nombre"]."', '".$_POST["apellido"]."')
		";
		$statement = $conexion->prepare($query);
		$statement->execute();
		echo '<p>Insertado con Exito...</p>';
	}
}
?>