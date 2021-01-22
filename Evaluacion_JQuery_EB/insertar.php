<?php
    include('coneccionBD.php');
    if(isset($_POST["action"]))  {
	if($_POST["action"] == "insert") {
		$query = "
		INSERT INTO alumnos (codigo, nombres, telefono, direccion) VALUES ('".$_POST["codigo"]."', '".$_POST["nombres"]."', '".$_POST["telefono"]."','".$_POST["direccion"]."')";
		$statement = $conexion->prepare($query);
		$statement->execute();
		echo '<p>Insertado con Exito...</p>';
	}
}
?>