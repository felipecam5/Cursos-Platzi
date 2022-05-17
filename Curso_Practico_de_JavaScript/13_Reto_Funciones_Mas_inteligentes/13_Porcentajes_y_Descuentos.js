function CalcularPrecioFinal(original,descuento)
{
    if(original == "" || descuento =="")
    {
        return ("Hay un camplo sin completar por lo que no se puede realizar el calculo")
    }
    else if( original < 0 || descuento < 0){
        return ("No se admiten valores negativos en ninguno de los campos")
    }
    else{
        
        return ("El valor con un descuento del " + String(descuento) + "(%)" + " para el producto con valor original de " + Number(original) + " es " + ((Number(original)) * (100- Number(descuento)))/100 );

    }
    
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

var cupones =["DragonBallZ", "Goku", "Checgod", "NoTengoDescuento"]

function descuentocupon(original, descuento, descupon)
{
    if(descupon == "")
    {
        return("No tiene ningun cupon que se pueda aplicar al producto")
    }

    else if(cupones.includes(descupon) == false )
    {
        return "El Cupon ingresado es incorrecto o no existe"
    }
    else if(original == "" || descuento =="")
    {
        return ("Hay un camplo sin completar por lo que no se puede realizar el calculo")
    }
    else if( original < 0 || descuento < 0)
    {
        return ("No se admiten valores negativos en ninguno de los campos")
    }
    else if(descupon == cupones[0])
    {
        return ("El valor con un descuento del " + String(descuento) + "(%)" + " y un cupon adicional del 5(%)"    + " para el producto con valor original de " + Number(original) + " es " + ((Number(original)) * (100- (Number(descuento)+5)))/100 );
    }
    else if(descupon == cupones[1])
    {
        return ("El valor con un descuento del " + String(descuento) + "(%)" + " y un cupon adicional del 10(%)"    + " para el producto con valor original de " + Number(original) + " es " + ((Number(original)) * (100- (Number(descuento)+10)))/100 );
    }
    else if(descupon == cupones[2])
    {
        return ("El valor con un descuento del " + String(descuento) + "(%)" + " y un cupon adicional del 15(%)"    + " para el producto con valor original de " + Number(original) + " es " + ((Number(original)) * (100- (Number(descuento)+15)))/100 );
    }
    else if(descupon == cupones[3])
    {
        return ("El valor con un descuento del " + String(descuento) + "(%)" + " y un cupon adicional del 20(%)"    + " para el producto con valor original de " + Number(original) + " es " + ((Number(original)) * (100- (Number(descuento)+20)))/100 );
    }
    
    
}

function CalcularPrecioCuponHTML(){
    var value1 = document.getElementById("PrecioOriginal");
    var value2 = document.getElementById("Descuento");
    var value3 = document.getElementById("Cupon");

    var original = value1.value;
    var descuento =value2.value;
    var cupon = value3.value;

    var valorfinal = descuentocupon(original,descuento,cupon);

    var resultado = document.getElementById("Result");

    resultado.innerText = valorfinal;
}

