<?php
    include('coneccionBD.php');
    if (isset($_POST['id'])){
		$id = $_POST['id'];
		$codigo = $_POST['codigo'];
		$nombres = $_POST['nombres'];
		$telefono = $_POST['telefono'];
		$direccion = $_POST['direccion'];
        $query = "UPDATE alumnos SET codigo = '$codigo',nombres = '$nombres', telefono ='$telefono', direccion ='$direccion' WHERE id ='$id'";
        $resultado = mysqli_query($conexion, $query);

        if(!$resultado){
            die('sentencia ha fallado');
        }
        echo "Se actualizo correctamente";
    }	
?>
