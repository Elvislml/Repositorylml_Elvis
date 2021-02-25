<?php
$conexion=mysqli_connect('localhost','root','','trabajoorm',3307); 
    $nombre = $_POST['nombre'];
    $apellido = $_POST['apellido'];
    $usuario = $_POST['usuario'];
    $password = $_POST['password'];

    $sql = "insert into tabla (nombre, apellido, usuario, password) 
            values ('$nombre','$apellido','$usuario', '$password')";
    echo mysqli_query($conexion,$sql);

?>