function observarResultado(){
    return(document.getElementById("resultado").innerHTML);
}

function escribirResultado(value){
    document.getElementById("resultado").innerHTML = value;
}

function add(key){
    var result = observarResultado();
    if (result !='0' || isNaN(key)) {
        escribirResultado(result + key);
    }else{
        escribirResultado(key);
    }
}

function calcular(){
    var resp = eval(observarResultado());
    escribirResultado(resp);
}

function limpiar(){
    escribirResultado(null);
}

function raiz(){
    var result = observarResultado();
    var raiz = Math.sqrt(result);
    escribirResultado(raiz);
}