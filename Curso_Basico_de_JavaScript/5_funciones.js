//Declarativas

function miFuncion (){
    return 3;
}


//Expresion

var miFuncion = function(a,b){
    return a+b;
}

function saludarestudiantes(estudiante){

    console.log(estudiante)
}

function saludarestudiantes2(estudiante){

    console.log(`hola ${estudiante}`); 
}

function sumar (a,b){
    var resultado = a+b;
    return "El Resultado de sumar " + String(a) + " y " + String(b) + " es "  + resultado;
}