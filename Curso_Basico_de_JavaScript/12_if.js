//Estructura if


var a = 5;
if (a>10){

    a = 1;
}
else{
    a += 1; 

}

var a = 0;
function prueba(b)
{
    
    var c = a + b;
    if(c < 10)
    {       
        a += 1;
        return "Operación Completada" + a;
    }
    else
    {
        return "Paila" + c;
    }

}

// Ahora si clase
if (true){
    console.log ("Hola");
}
// Estructura else-if
if (true){
    console.log ("Hola");
}
else{
    console.log ("Soy falso");
}

//Ciudadano puede votar

function votacion(a){
    if (a >= 18)
    {
        return "El ciudadano puede votar";
    }
    if (a == 17)
    {
        return "El ciudadano puede votar apartir del proximo año";
    }
    else if (a < 17)
    {
        return "El ciudadano no puede votar";
    }
    else
    {
       return "El ciudadano está muerto";
    }
}

//Ejemplo piedra papel o tijera

var op1 = "Piedra";
var op2 = "Papel";
var op3 = "Tijera";

var resultado = function(user, cpu){
    if(user != cpu){
        if(user === op1 && cpu === op3){
            console.log("el usuario GANO con "+ op1)
        }else if(user === op2 && cpu === op1){
            console.log( "el usuario GANO con " + op2)
        }else if(user === op3 && cpu === op2){
            console.log("el usuario GANO con " + op3)
        }else{
            console.log("La CPU Gano!!")
        }
    }else if(user === cpu){
        console.log("Empate")
    }
};

resultado(op1,op3) //el usuario GANO con Piedra```


//JUEGO PIEDRA PAPEL O TIJERA (FELIPE CAMACHO)

var opcion1 = "Piedra";
var opcion2 = "Tijera";
var opcion3 = "Papel";

function juego(Persona, Computadora){
    if (Persona != Computadora){
        if (Persona == opcion1 && Computadora == opcion2)
        {
            return "Gana Persona, con Piedra"
        }
        else if (Persona == opcion1 && Computadora == opcion3)
        {
            return "Gana Computador, con Papel"
        }
        else if (Persona == opcion2 && Computadora == opcion1)
        {
            return "Gana Computadora, con Piedra"
        }
        else if (Persona == opcion2 && Computadora == opcion3){
            return "Gana Persona con Tijera"
        }
        else if (Persona == opcion3 && Computadora == opcion1)
        {
            return "Gana Persona, con Papel"
        }
        else (Persona == opcion3 && Computadora == opcion2)
        {
            return "Gana Computadora, con tijera"
        }
    }
    else{
        return "Empate"
    }

}