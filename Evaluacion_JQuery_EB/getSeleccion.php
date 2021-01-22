<?php
    include('coneccionBD.php');
    
    if (isset($_POST['id'])) {
        $query = "SELECT * FROM alumnos WHERE id = " . $_POST['id'];
        $result = mysqli_query($conexion,$query);    
        if(!$result){
            die('Query con problemas' . mysqli_error($conexion));
        }
        $json = array();
        while ($row = mysqli_fetch_array($result)) {
            $json[]= array(
                'codigo'=>$row['codigo'],
                'nombres'=>$row['nombres'],
                'telefono'=>$row['telefono'],
                'direccion'=>$row['direccion'],
                'id'=>$row['id']
            );
        }
    }
    $jsonstring = json_encode($json[0]);
    echo $jsonstring;
?>
