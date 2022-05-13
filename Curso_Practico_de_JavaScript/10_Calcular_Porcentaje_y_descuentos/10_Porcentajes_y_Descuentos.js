function CalcularPrecioFinal(original,descuento)
{
    return ("El valor con un descuento del " + String(descuento) + "(%)" + " para el producto con valor original de " + Number(original) + " es " + ((Number(original)) * (100- Number(descuento)))/100 );
}

function CalcularPrecioFinalHTML(){
    var value1 = document.getElementById("PrecioOriginal");
    var value2 = document.getElementById("Descuento");

    var original = value1.value;
    var descuento =value2.value;

    var valorfinal = CalcularPrecioFinal(original,descuento);

    var resultado = document.getElementById("Result");

    resultado.innerText = valorfinal;
}
