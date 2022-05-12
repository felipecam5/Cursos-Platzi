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

var CarrosUltimoModelo = CarrosEnCasa.find(function(carro){
    return carro.Modelo == "2019"; //Metodo de Filtrado que retorna solo el primer valor coincidente
});

CarrosEnCasa.forEach(function(carro){
    console.log(carro.nombre + carro.Modelo);    
}); //Retorna solo el valor en consola

var carrosviejos = CarrosEnCasa.some(function(carro){
    return carro.nombre == "Test2";
}); //Retorna solo True o False
