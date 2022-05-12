var frutas = ["Maracuya"];
function agregarfrutas(a)
{
           
    if (frutas.includes(a))
    {
        return "La Fruta " + a + " ya existe en el carrito";  
    }
    else
    {
        frutas.push(a);
        return "La fruta " + a + " fue agregada al carrito";    
    }
}

function imprimiruno(frutas)
{
    return  console.log (` Las frutas en el carro de mercado son: ${frutas}`);
}

function carromercado()
{
    for (var i=0; i<frutas.length;i++)
    {
        imprimiruno(frutas[i]);
    }
}

carromercado()


function print()
{
    return console.log(`${frutas}`)
}

var miauto = {
    marca: "Volskwagen",
    modelo: "T-cross",
    annio: 2020,
    informacion: function()
    {
        return console.log(`El carro ${this.marca} es del año ${this.annio} y es la referencia ${this.modelo}`)
    }
};

var maestria = {
    nombre: "GeoVisualization and Geocomunitcation",
    duracion: 2,
    creditos: 160,
    informacion: function()
    {
        return console.log(`La maestria ${this.nombre} tiene una duracion de ${this.duracion} años y tiene ${this.creditos} creditos`)
    }
}

function pilotos(nombre, apellido, puntos)
{
    this.nombre = nombre;
    this.apellido = apellido;
    this.puntos = puntos;
}

var Verstappen = new pilotos("Max", "Verstappen", 56);
var Checho = new pilotos("Sergio", "Perez", 30);
var Alonso = new pilotos("Fernado", "Alosno", 84);

//Siguiente//

var cursos = ["SQL", "HMTL", "CSS"]
var duraciones = [15,25,32]
var instructores = ["Isreal", "Freddy", "Camila"]

function platzicursos (curso, duracion, instructor)
{
    this.curso = curso;
    this.duracion = duracion;
    this.instructor = instructor;
};

for(var i = 0; i<cursos.length; i++)
{
    this["Curso" + duraciones[i]] = new platzicursos(cursos[i], duraciones[i], instructores[i]);
}

//Filtrado//

var mayor20 = cursos.filter(function(cursos)
{
    if (cursos.duraciones > 20)
    {
        return cursos.nombre;
    }
});