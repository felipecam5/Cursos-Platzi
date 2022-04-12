var CarrosEnCasa = [
    carroFelipe = {
        nombre: "Test",
        Modelo: "2020"
    },
    carroRomulo = {
        nombre: "Test2",
        Modelo: "2019"
    } ,
    carroJulian = {
        nombre: "Test2",
        Modelo: "2019"
    } ,
    carroMaps = {
        nombre: "Test2",
        Modelo: "2242"
    } ,
    carroJuliana = {
        nombre: "Test2",
        Modelo: "2142"
    } ,
    carroJAlejo = {
        nombre: "Test2",
        Modelo: "2081"
    } 


]

var CarrosUltimoModelo = CarrosEnCasa.filter(function(carro){
    return carro.Modelo == "2019"; //Metodo de Filtrado
});

//Metodo de Mappeo

var nombre_carro = CarrosEnCasa.map (function(carro){
    return carro.nombre;
});

