//VARIABLES Y OPERACIONES

//1. ¿Qué es una variable y para qué sirve?
  
    //Una variable es un elemento utilizado en programación para guardar en memoria valores que deban ser reutilizados.
   
 //2. ¿Cual es la diferencia entre declarar e inicializar una varible.
 
    // Declarar es cuando creas la variable pero sin asignarle valor alugno, mientras que inicializar hace referencia a darle un valor.

//3. ¿Cual es la diferencia entre sumar números y concatenar strings?

    // Mientras que sumar variables int da como resultado el valor de la operación matematica correspondiente,
    // concatenar strings adjunta los caracteres, los pone de manera adjacente
    // Ej 2+5 = 7 || 2 +"5" = 25

//4. ¿Cual operador me permite sumar o concatenar?

    //El operador de suma (+)

//5. Detemermine el nombre y tipo de dato para almancenar en variables la siguiente informacion
//6. Traduce a código JavaScript las variables del ejemplo anterior y deja tu código en los cometnarios

var Nombre = "Felipe" //String
var Apellido = "Camacho Hurtado" //String
var Nombre_de_Usuario_en_Platzi = "Felipecam5" //String
var Edad = 20 //Numero
var Correo_Electronico = "fcam_5@hotmail.com" //String
var Mayor_de_Edad = true //Boolean
var Dinero_ahorrado = 1500000 //Numero
var Deudas = 450000 //Numero

//7. Calcula e imprime las siguientes variables a partir de las variables del ejemplo anterior:

var Nombre_Completo = console.log(`${Nombre} ${Apellido}`);
var Dinero_Real = console.log(Dinero_ahorrado - Deudas);

//FUNCIONES

//1. ¿Que es una función?

    //Conjuntos de sentencias que pueden utilizarse con los valores guardados
    //anteriormente para retornar o validar mas información.

//2. ¿Cuando me sirve una función en mi código?

    //Cuando deseo automatizar operaciones o acciones para obtener mayor información

//3. ¿Cual es la diferencia enetre parámetros y argumentos de una función?

    //Los parametros son los variables requeridas para el uso de la funcion
    // Mientras que lso argumentos son en si los valores utilizados al momento de invocarla.

//4.Convierte el siguiente código en una función,
//pero, cambiando cuando sea necesario las variables constantes por parámetros y argumentos en una función: 

var nombre="";
var apellido= "";
var nickname = "";
var Nombre_Completo = nombre + apellido

function datospersonales(nombre,apellido,nickname)
{
    var Nombre_Completo = nombre + " "+ apellido
    return console.log(`Mi nombre es ${Nombre_Completo}, pero prefiero que me digas ${nickname} .`)
}

//CONDICIONALES

    //1. ¿Que es una condicional?

        //Es un operador que permite ejecutar una acción siempre y cuando se cumpla el caso favorable

    //2 ¿Que tipos de condicionales existen en JavaScript y cuales son sus diferentecias?
    
        //IF: Si se cumple, entra a ejecutar el codigo.
        //ELSE: Si no se cumple ninguna condicion previa, ejecuta este codigo
        //ELSE IF: Si no se cumple la condicion anterior, ejecuta este codigo.

    //3. ¿Puedo combinar funciones y condicionales?
    
        //Claro

    //4. Replica el comportamiento del siguiente código que usa la sentencia switch utilizando if, else y else if:    
    
var tipoDeSuscripcion = "Basic"

function beneficios()
{
    if(tipoDeSuscripcion == "Free")
    {
        return console.log(`Solo puedes tomar los cursos gratis`)
    }
    else if(tipoDeSuscripcion == "Basic")
    {
        return console.log(`Puedes tomar casi todos los cursos de platzi durante un mes`)
    }
    else if (tipoDeSuscripcion == "Expert")
    {
        console.log(`Puedes tomar casi todos los cursos de Platzi durante un año`)
    }
    else (tipoDeSuscripcion == "ExpertPlus")
    {
        return console.log(`Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año`)
    }

}

    //5. Replica el comportamiento de tu condicional anterior con if, else y else if, pero ahora solo con if (sin else ni else if).

    function beneficios()
{
    if(tipoDeSuscripcion == "Free")
    {
        return console.log(`Solo puedes tomar los cursos gratis`)
    }
    if(tipoDeSuscripcion == "Basic")
    {
        return console.log(`Puedes tomar casi todos los cursos de platzi durante un mes`)
    }
    if (tipoDeSuscripcion == "Expert")
    {
        console.log(`Puedes tomar casi todos los cursos de Platzi durante un año`)
    }
    if(tipoDeSuscripcion == "ExpertPlus")
    {
        return console.log(`Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año`)
    }

}

    //6. BONUS: Replicar este comportamiento con arrays y un solo condicional. 

    var tiposub = "Basic";
    var planes =["Free", "Basic", "Expert", "ExpertPlus"];
    var mensajes = ["Solo puedes tomar los cursos gratis",
    "Puedes tomar casi todos los cursos de Platzi durante un mes",
    "Puedes tomar casi todos los cursos de Platzi durante un año",
    "Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año"];
    var index = planes.indexOf(tiposub)

    if(index == -1)
    {
        console.log(`No existe este plan`)
    }
    else
    {
        console.log(mensajes[index])
    }

//Ciclos

    //1. ¿Que es un ciclo?
        
        //Son elementos que permiten recorrer todo un conjuntos de datos hasta cumplir cierta condicion, ejecutando codigo.

    //2. ¿Qué tipos de ciclos existen en JavaScript?

        //For
        //For of
        //While
    //3. ¿Que es un cliclo infinito y por qué es un problema?

        //Es un ciclo en el cual nunca se cumpla la condicion de quiebre por lo que se ejecutará
        //Infinitamente hasta que el usuario o la maquina lo paren.
            
    //4. ¿Puedo mezclar ciclos y condicionales?

        //Si

    //5. Replica el comportamiento de los siguientes ciclos for utilizando ciclos while:    

var i = 0;
while (i < 5)
{
    console.log(`El valor de i es ${i}`);
    i++;
} 

var i = 10;
while (i>=2)
{
    console.log(`El valor de i es: ${i}`);
    i --;
}

    //6. Escribe un código en JavaScript que le pregunte a los usuarios cuánto es 2 + 2. Si responden bien, mostramos un mensaje de felicitaciones,
    // pero si responden mal, volvemos a empezar.

var pregunta = prompt("¿Cuanto es dos(2) + dos(2)");

if(pregunta == 4)
{
    console.log(`Felicitaciones, tu respuesta es correcta`);
}
else{
    console.log(`Lo siento, tienes que seguir practicando`)
}

//LISTAS

//1. ¿Qué es un array?

    //Es una lista de valores

//2. ¿Qué es un objeto?

    //Es un grupo de elementos(arrays), que comparten atributos similares.

//3. ¿Cuándo es mejor usar objetos o arrays?

    //Arrays cuando no hay caracteristicas similares y objectos cuando si.

//4. ¿Puedo mezclar arrays con objetos o incluso objetos con arrays?

    //Si

//5. Crea una función que pueda recibir cualquier array como parámetro e imprima su primer elemento.


function Array(a)
{
    return console.log(`${a}`)
}
//6. Crea una función que pueda recibir
//cualquier array como parámetro e imprima todos
//sus elementos uno por uno (no se vale imprimir el array completo).




function des(a)
{
    for(var i = 0; i < a.length; i++ )
    {
        Array (a[i]);
    }
}

//7.Crea una función que pueda recibir cualquier objeto
//como parámetro e imprima todos sus elementos
//uno por uno (no se vale imprimir el objeto completo).

var equipos= [
    oncecaldas = {
        ciudad: "Manizales",
        estadio: "Palogrande",
        hinchas: 30000
    },
    Santafe={
        ciudad: "Bogotá",
        estadio: "Nemesio",
        hinchas: 50000
    }

]

equipos.forEach(function(equipo)
{
    console.log(equipo);
});