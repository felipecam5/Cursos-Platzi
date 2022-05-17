//Ejemplos de uso con array.map

//1.Suma
numeros = [1,5,6,7,10,11];
suma = 0;

function sumas(elemento)
{
    suma=0;
    elemento.map(function(numero)
    {
        suma +=numero;
        console.log(suma)
        
    }
    )
}


//2.Multiplicación

var NumerosMulti = [1,4,5,6,11,24];

var resultado = NumerosMulti.map(function(elemento){
    return elemento*100;
})

var prueba =[];
function multipli(lista)
{
    prueba= lista.map(function(elemento)
    {
        return elemento*4;
    }
    )
}

//3.Parejas

var prueba2 =[0,4,5,6];

    var ls = prueba2.map(function(elemento)
    {
        return [elemento,elemento];
    }
    )

var ele = []
function parejas(lista){
    ale = lista.map(function(elemento)
    {
        return [elemento,elemento];
    })
}    

//4.Concatenación

var ciudadanos =[
    {nombre : "Felipe",apellido: "Camacho",ciudad: "Bogota"},
    
    {nombre: "Andres", apellido: "Hurtado",ciudad: "Bogota"}
];

var nya = ciudadanos.map(function(elemento)
{
    return elemento.nombre +  " " + elemento.apellido;   
})


//5.Promedio
var prom = 0;

function promed(lista){
    lista.map(function(elemento)
    {
        return prom+=elemento;
    })

    prom = prom/2;
    console.log(prom);
}


//CLASE: CALCULANDO MODA

var lista1 = [1,3,32,4,5,5,6,2,1];

var lista1Count = {};

lista1.map(function(elemento)
{
    if(lista1Count[elemento])
    {
        lista1Count[elemento] += 1;
    }
    else
    {
        lista1Count[elemento]=1;
    }
    
}
)

var lista2 =[];

lista2 = Object.entries(lista1Count);

lista3= lista2.sort(
    function(elementoA,elementoB)
    {
        return elementoB[1] - elementoA[1];
    }
)

var lista4 = lista3[0];

//RETO: Calculando Moda con Parametros

var listamoda = {};
var lmoda =[]

function ValoresModa(lmoda)
{
    
    lmoda.map(function(elemento)
    {
        if(listamoda[elemento])
    {
        listamoda[elemento] += 1;
    }
    else
    {
       listamoda[elemento]=1;
    }    
    }
    )
    var lista10 = [];
    lista10 = Object.entries(listamoda);
    lista5= lista10.sort(
        function(elementoA,elementoB)
        {
            return elementoB[1] - elementoA[1];
        }
    )
    
    var lista6 = lista5[0];
    return lista6;

};    

//Reto Promedio ponderado

var cursos = [
    {nota:4.5, creditos:2}, {nota:3.2, creditos:3}, {nota:2.1, creditos:4}
];

var producto = []

producto = cursos.map(function(e)
{
    return (e.nota*e.creditos);
})

var sumaproducto = 0;

producto.map(function(e)
{
    sumaproducto += e
})

var sumacreditos = 0

cursos.map(function(e)
{
    sumacreditos += Number(e.creditos);        
})

var promedioponderado = 0;

promedioponderado = sumaproducto/sumacreditos;
