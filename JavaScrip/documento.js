function saludar(){
    alert("Hola mi primer scrpt");
}

function sumar(){
    num1 = parseInt(document.getElementById("n1").value);
    num2 = parseInt(document.getElementById("n2").value);
    resul = num1 + num2;
    alert("La suma es ==>" + resul);
}

function invertirCadena(){
    var  cadenaObtenida = document.getElementById("cadena").innerText;
    var vector = cadenaObtenida.split(''); //arreglo de caracteres
    var reversa = vector.reverse(); //invertir la cadea
    var cadenaInvertida = reversa.join(''); //Une el arreglo en una sola cadena
    document.write(cadenaInvertida);
}

function validacion(){
    var nombres = document.getElementById("nombres").value;
    if(nombres== ""){
        alert("Por favor digite el usuario");
    }
}