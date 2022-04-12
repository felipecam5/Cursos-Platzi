var estudiantes = ["Maria", "Sergio", "Carlos"];

function saludo (estudiante){
    return console.log(`Bienvenido al curso ${estudiante}`)
}

while(estudiantes.length > 0)
{
    console.log(estudiantes)
    var estudiante = estudiantes.shift()
    saludo(estudiante)

}