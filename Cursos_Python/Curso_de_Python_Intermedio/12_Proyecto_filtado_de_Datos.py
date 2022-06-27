from unicodedata import name


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

# RETO: Retornar los nombres de aquellos quienen manejen python.

def reto_previo():
    for i in DATA:
        for key,value in i.items():
            if key == "language" and value == "python":
                print(f'{i["name"]} maneja Python')

# Implementación Clase

def run():
    
    #Utilizando list comprehension

    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    print(f'Aquellos que manejan el lenguaje de python son: {all_python_devs}')
    
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    print(f'Aquellos que trabajan en platzi son: {all_platzi_workers}')

    #Utilizando Filter encontrar aquellos mayores de 18 años

    adults = list(filter(lambda worker: worker["age"] >=18, DATA))
    adults = list(map(lambda worker : worker["name"], adults))
    print(f' Aquellos que son adultos son: {adults}')
    old_people = list(map(lambda worker: worker | {"old": worker["age"] >= 70}, DATA))
    print(f'El nuevo diccionario es: {old_people}')

    #RETOS FINALES

    #1. Crear la lista all_python_devs usando filter() y map()

    all_python_devs_reto = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs_reto = list(map(lambda worker: worker["name"], all_python_devs_reto))
    print(f'Los desarrolladores de python son: {all_python_devs_reto}')

    #2. Crear la lista all_Platzi_workers usando filter() y map()

    all_platzi_workers_reto = list(filter( lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers_reto = list(map(lambda worker: worker["name"], all_platzi_workers_reto))
    print(f'Los trabajadores en platzi son: {all_platzi_workers_reto}')

    #3 Crear la lista old_people con list comprehensions

    old_people_reto = list(worker | {"old": worker["age"] >=30 } for worker in DATA)
    print(f'El nuevo diccionario es {old_people_reto}')

    #4 Crear la lista adults con list comprehensions

    adults_reto = list(worker["name"] for worker in DATA if worker["age"] >= 18)
    print(f'Los miembros del equipo que ya cumplieron la mayoria de edad son: {adults_reto}')

if __name__ =="__main__":
    reto_previo()
    run()