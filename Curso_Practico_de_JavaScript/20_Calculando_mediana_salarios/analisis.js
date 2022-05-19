var SalariosColombia = [];

var SalariosColombia = colombia2.map(function(elemento)
{
    return elemento.salary;
});

var SalariosColOrdenado = [];

SalariosColOrdenado = SalariosColombia.sort((a,b)=> b-a);

function esPar(numero){
    return (numero % 2 == 0)
}

function CalculoMediana(lista)
{
    var mediana = 0;
    var mitad = parseInt(lista.length/2)
    var mitadmenosuno = parseInt(lista.length/2) -1
    

    if(esPar(lista.length) == true)
    {
        mediana = (lista[mitad] + lista[mitadmenosuno])/2;
        return(mediana);
    }
    else
    {
        mediana = lista[mitad];
        return (mediana);
    }
}

var medianaGeneralColombia = CalculoMediana(SalariosColOrdenado)
var spliceStart = (((SalariosColOrdenado.length)*90)/100);
var spliceCount = SalariosColOrdenado.length - spliceStart;

var SalariosColTop10 = SalariosColOrdenado.splice(spliceStart,spliceCount);