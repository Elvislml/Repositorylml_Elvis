<?php
	include('coneccionBD.php');
	if (isset($_POST['search'])) {
		$search = $_POST['search'];
		$query = "SELECT * FROM alumnos WHERE nombres LIKE '$search%'";
		$resultado = mysqli_query($conexion, $query);

		if(!$resultado){
			die('Error en la buqueda');
		}
    }

    $json = array();
	while ($row = mysqli_fetch_array($resultado)) {
		$json[]= array(
            'codigo'=>$row['codigo'],
			'nombres'=>$row['nombres'],
            'telefono'=>$row['telefono'],
            'direccion'=>$row['direccion'],
			'id'=>$row['id']
		);
	}
	$jsonstring = json_encode($json);
	echo $jsonstring;
    
?>