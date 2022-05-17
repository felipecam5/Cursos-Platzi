var lista = [
    100,
    200,
    500,
    4000000,
    2,
    150,
    3200,
    5000
]

var mitadLista1 = lista.length/2;

function esPar(numerito)
{
    if(numerito % 2 === 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

var mediana;

if(esPar(lista.length) == true)
{
    lista.sort((a,b)=>b-a);
    mediana = ((lista[mitadLista1] + lista[mitadLista1-1])/2 );
    console.log (mediana);
    console.log(lista);
}
else
{
    mediana = (lista[parseInt(mitadLista1)])
}


//Reto: Crear una función que reciba cualquier array como parametro.

//1. Arreglo de prueba.

var lista = [2,4,5,6,7,34,31,90,70];

//2. Funcion par/impar

function esPar(lista)
{
    if(lista % 2 === 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

//3. Calculo Mediana

var posicion1 = lista[parseInt(lista.length/2)]; //Devuelve el elemento en la mitad
var posicion0 = lista[parseInt((lista.length/2)-1)]; //Devuelve el elemento en la mitad - 1
var mediana = 0; //Variable para guardar el valor de la mediana.

if(esPar(lista.length) == true)
{
    lista=lista.sort((a,b)=>b-a)
    mediana = (posicion1 + posicion0)/2;
    console.log(mediana);

}
else
{
    lista=lista.sort((a,b)=>b-a)
    mediana = posicion1;
    console.log(mediana);
}

//4. Funcion autonoma

function esPar(lista)
{
    if(lista % 2 === 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

function CalculoMediana(listado)
{
    var posicion1 = listado[parseInt(listado.length/2)]; //Devuelve el elemento en la mitad
    var posicion0 = listado[parseInt((listado.length/2)-1)]; //Devuelve el elemento en la mitad - 1
    var mediana = 0; //Variable para guardar el valor de la mediana.

    if(esPar(listado.length) == true)
{
    listado=listado.sort((a,b)=>b-a)
    mediana = (posicion1 + posicion0)/2;
    return "la lista " + listado + " tiene como mediana el valor de " + mediana;

}
else
{
    listado=listado.sort((a,b)=>b-a)
    mediana = posicion1;
    return "la lista " + listado + " tiene como mediana el valor de " + mediana;
}
}
