//En este ejercicio debes crear una función para calcular la altura de un triángulo isósceles.
//La función debe recibir, como parámetros, la longitud de los 3 lados del triángulo.
//La función debe validar que la longitud de los 3 lados del triángulo corresponden a un triángulo isósceles.
//La función debe retornar la altura del triángulo.
//Pista: la función Math.sqrt de JavaScript puede ayudarte a calcular raíces cuadradas.

function alturaIsosceles()
{
    var longitudlado1 = prompt("Por favor indique la longitud del primer lado del triangulo");
    var longitudlado2 = prompt("Por favor indique la longitud del segundo lado del triangulo");
    var base = prompt("Por favor, indique la longitud de la base del triangulo ");

    if( longitudlado1 == longitudlado2)
    {
        if(longitudlado1 != base)
        {
            return console.log("La altura del triangulo isosceles de lados " + Number(longitudlado1) + "," + " y base " + Number(base) + " es " + Math.sqrt((longitudlado1*longitudlado2) - ((base*base)/4)))
        }
        else{
            return console.log("La base mide igual que alguno de los lados por lo que no se puede calcular la altura de este tipo de triangulo");
        }
    }
    else
    {
        return console.log ("Los lados de los triangulos no son congruentes, por lo que no se puede calcular la altura de este tipo de triangulo");
    }
}