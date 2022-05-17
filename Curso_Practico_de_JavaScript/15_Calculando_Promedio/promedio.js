//Estatico
var valores = [0,1,3,4,5,8];

function CalcularPromedio()
{
    resultado = 0;
    for( var i=0 ; i < valores.length; i++)
    {
        resultado = resultado + valores[i];
        console.log(resultado);
           
    }
    promedio = resultado/valores.length
    console.log(promedio);
    
}

//Dinamico

function MediaAritmetica(lista)
{
    var suma = 0;

    for(var i=0; i<lista.length;i++)
    {
        suma = suma + lista[i];
    }
    
    var promediolista = suma/lista.length;
    return promediolista;
}

var listanu = []

function agregaelementos(lista)
{
    listanu.push(lista)
}

function agrega(lista)
{
    for(i=0; i< lista.length;i++)
    {
        listanu.push(lista[i])
    }
}

//Como Funcional el array.reduce.

var listareduce =[0,4,5,6];

function suma(valora,valorb)
{
    return valora + valorb;
}

var concat = listareduce.reduce(suma);

console.log(concat);

//Promedio estatico con array.reduce

var listareduce = [3,5,6,7,2];

function sumareduce(a,b){
    return a+b;
}

var suma = listareduce.reduce(sumareduce);

console.log(suma/listareduce.length);

//Promedio estatico con array.reduce segun platzi.

var lista = [3,5,6,7,2];

var sumlista = lista.reduce(
    function(valoracumulado = 0, nuevoelemento)
    {
        a = valoracumulado + nuevoelemento;
        return a;
        
    }
)

var resultado = a;

console.log(a/lista.length)








