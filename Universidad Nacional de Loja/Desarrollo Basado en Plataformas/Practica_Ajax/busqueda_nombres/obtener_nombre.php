<?php
    $resultado = "";
    $nombre = $_GET['nombre'];
    $arreglo = array("Martha","Juana","Valeria","Jessybel");
    for($i=0; $i < count($arreglo); $i++){
        if($nombre == $arreglo[$i]){
            $resultado = "<p>El nombre: $nombre ha sido encontrado u.u</p>";
        }
    }
    if($resultado == ""){
        echo "No existe $nombre en el servidor";
    }else{
        echo "Hola, te saludamos: " . $resultado;
    }
?>
