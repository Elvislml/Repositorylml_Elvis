document.write("<h2>Tabla de Multiplicar</h2>")
document.write("<table class ='table table-striped'><tr><td>Serie</td><td>Resultado</td></tr>");
var input = parseInt(prompt("Ingrese la serie a generar"));
var resultado = "";
for(i = 1; i <= 12; i++){
    resultado += '<tr><td>' + input + '*' + i +'='+'</td> <td>' + (input * i) + '</td></tr>';
}
document.write(resultado);
document.write("</table>");