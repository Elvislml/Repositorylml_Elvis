<?php
    include('coneccionBD.php');

    if (isset($_POST["action"])) {
        if($_POST["action"] == "seleccion_persona"){
		$query = "
		SELECT * FROM persona WHERE id = '".$_POST["id"]."'
		";
		$statement = $conexion->prepare($query);
		$statement->execute();
		$result = $statement->fetchAll();
		foreach($result as $row){
			$output['nombre'] = $row['nombre'];
			$output['apellido'] = $row['apellido'];
		}
		echo json_encode($output);
	}
	if($_POST["action"] == "update"){
		$query = "
		UPDATE persona 
		SET nombre = '".$_POST["nombre"]."', 
		apellido = '".$_POST["apellido"]."' 
		WHERE id = '".$_POST["hidden_id"]."'
		";
		$statement = $conexion->prepare($query);
		$statement->execute();
		echo '<p>Data Updated</p>';
	}
}
?>