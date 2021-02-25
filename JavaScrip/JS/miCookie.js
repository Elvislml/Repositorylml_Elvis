function setCookie(nombre, valor, expiracion){
    var d = new Date();
    d.setTime(d.getTime() + expiracion*24*60*60*100);
    var expirar ="expires="+d.toUTCString;
    document.cookie = nombre +"=" + valor +";"+ expirar + ";path=/";
}

function getCookie(nombre){
    var nom = nombre + "=";
    var array = document.cookie.split(";");
    for(var i = 0; i<array.length; i++){
        var c = array[i];
        while(c.charAt[0] == " ") {
            c = c.substring(1);
        }
        if(c.indexOf(nombre) == 0){
            return c.substring(nombre.length, c.length);
        }
    }
    return "";

}

//Propios metodos
var verCookies = function(){
    alert("Las cookies actuales son:\n" + document.cookie);
}

var crear = function(){
    var nombre = prompt("Ingresar el nombre de la cookie");
    var valor = prompt("Ingresar el valor de la cookie");
    var expiracion = prompt("Ingresar el # de días de la cookie");
    setCookie(nombre, valor, expiracion);
}

var eliminar = function(){
    var nombre = prompt("Ingrese el nombre de la cookie para eliminar");
    setCookie(nombre,"",0);
}

var buscar = function(){
    var nombre = prompt("Ingrese el nombre de la cookie para buscarla");
    var resultado = getCookie(nombre);
}


window.onload = function(){
    var botonVC = document.getElementById("verTodas");
    botonVC.onclick = function(){
        verCookies();
    };

    var botonCC = document.getElementById("crear");
    botonCC.onclick = function(){
        crear();
    };

    var botonMC = document.getElementById("modificar");
    botonMC.onclick = function(){
        crear();
    };
    var botonEC = document.getElementById("eliminar");
    botonEC.onclick = function(){
        eliminar();
    };

    var botonBC = document.getElementById("buscar");
    botonBC.onclick = function(){
        buscar();
    };
};



