var estudiantes = ["Felipe", "Maria", "Carlos", "Sebastian", "Nicolas"];

function saludarEstudiantes(estudiantes)
{
    return console.log (`Hola, ${estudiantes}`);
      // return "Hola, mi nombre es " + estudiantes; NO ME SIRVIO :()
}

for (var i= 0; i < estudiantes.length;i++) //RECOMENDADO
{
    saludarEstudiantes(estudiantes[i]);
    
}


for (var i of estudiantes) //NO RECOMENDADO
{
    saludarEstudiantes(i);
    
}
