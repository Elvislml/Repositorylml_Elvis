<?php
    include('coneccionBD.php');
	if (isset($_POST['id'])) {
		$id = $_POST['id'];
		$query = "DELETE FROM alumnos WHERE id = $id";
		$resultado = mysqli_query($conexion, $query);

		if(!$resultado){
			die('sentencia ha fallado');
		}
		echo "Eliminado con Exito";
	}
?>