//Pregunta Usuario Cuadrado

var pregunta = prompt("Por favor, indique la longitud de un lado del cuadrado para calcular area y perimetro de este.")

function areacuadrado()
{
    lado = prompt("Por favor, indique la longitud de un lado del cuadrado para calcular el area de este.")
    return "El Area de un Cuadrado de lado " + lado + " es " + lado*lado;
}

function perimetrocuadrado()
{
    lado = prompt("Por favor, indique la longitud de un lado del cuadrado para calcular el perimetro de este.")
    return "El Area de un Cuadrado de lado " + lado + " es " + lado*4;
}

function perimetrotriangulo()
{
    lado1 = prompt("Por favor, indique la longitud del lado (1) del triangulo")
    lado2 = prompt("Por favor, indique la longitud del lado (2) del triangulo")
    lado3 = prompt("Por favor, indique la longitud del lado (3) del triangulo")
    return "El perimetro del triangulo propuesto de lados " + String(lado1) + "," + String(lado2) + "," + String(lado3) +  " es " + (Number(lado1)+Number(lado2)+Number(lado3));
}

function areatriangulo()
{
    base = prompt("Por favor, indique la base del triangulo")
    altura = prompt("Por favor, indique la altura del triangulo")
    return "El area del triangulo propuesto de base " + String(base) + " y altura " + String(altura) + " es " + (Number(base) * Number(altura))/2;
}

function circunferenciacirculo()
{
    diametro = prompt("Por favor, indique el diametro del circulo")
    pi = 3.1416
    return "La circunferencia del Circulo propuesto de diametro " + String(diametro) + " es " + (Number(diametro) * pi);
}

function areacirculo()
{
    radio = prompt("Por favor, indique el radio del circulo")
    pi = 3.1416
    return "El area del Circulo propuesto de radio " + String(radio) + " es " + (Number(radio*radio) * pi);
}
