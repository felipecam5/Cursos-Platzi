function auto(marca, modelo, annio)
{
    this.marca = marca;
    this.modelo = modelo;
    this.annio = annio;
}

var carroFelipe = new auto("Volswagen", "T-Cross", 2020); //AÑADE LOS OBJETOS
var carroJulian = new auto("Volswagen", "T-Cross", 2020);
var carroRomulo = new auto("Volswagen", "T-Cross", 2020);
var carroAlejo = new auto("Volswagen", "T-Cross", 2020);

//Reto: Automatizarlo con un loop

var Marcas = ["Audi", "Ferrari", "Porche", "RedBull"];
var Conductor = [" Marcelo Vielsa", "Charles Lecrerc", "Mateo Matzi", "Max Verstappen"];
var Puntos = [0,20,18,34];

function escuderias (marcas, conductor, puntos){
    this.marca = marcas;
    this.conducutor = conductor;
    this.puntos = puntos;
}

for(var i = 0; i < Marcas.length; i++)
{
    
    this["carro"+ Marcas[i]] = new escuderias (Marcas[i], Conductor[i], Puntos[i]);
    console.log(Marcas[i]);
}