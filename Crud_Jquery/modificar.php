<?php
    include('database.php');
    if (isset($_POST['id'])){
        $id = $_POST['id'];
        $nombre = $_POST['name'];
        $descripcion = $_POST['description'];
        $query = "UPDATE task SET name = '$nombre', description ='$descripcion' WHERE id ='$id'";
        $resultado = mysqli_query($conexion, $query);

        if(!$resultado){
            die('sentencia ha fallado');
        }
        echo "Se actualizo correctamente";
    }	
?>