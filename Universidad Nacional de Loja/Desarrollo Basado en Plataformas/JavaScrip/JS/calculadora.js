function realizar_operacion(){
    var num1 = parseInt(document.getElementById("n1").value);
    var num2 = parseInt(document.getElementById("n2").value);
    var opcion = parseInt(document.getElementById("op").value)
    var resultado = 0;
    switch(opcion){
        case 1:
            resultado = num1 + num2;
            break;

        case 2:
            resultado = num1 - num2;
            break;

        case 3:
            resultado = num1 * num2;
            break;

        case 4:
            resultado = num1 / num2;
            break;
    }
    document.getElementById("resultado").innerText = resultado;
}