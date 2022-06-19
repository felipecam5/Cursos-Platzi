class Employee:
    #Constructor and Class Attributes
    def __init__(self, first, last, title, department):
        self.first = first
        self.last = last
        self.title = title
        self.department = department
        self.email = first.lower() + "." + last.lower() + "@gmail.com"
    
    # REGULAR METHODS
    def display_divider(self, arg_char = "-", line_lenght = 100):
        print(arg_char*line_lenght)

    def display_information(self):
        self.display_divider("-",45)
        print(f'Employee Information | {self.first} {self.last}'.center(45,' '))
        self.display_divider("-", 45)
        print(f'Title: {self.title} | Department: {self.department}')
        print(f'Email Address: {self.email}')

    # GETTERS > Obtiene un valor
    @property
    def fullname(self):
        print(f'{self.first} {self.last}')

    # SETTERS
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    # DELETERS > Cuando se quiere borrar una propiedad
    @fullname.deleter
    def fullname(self):
        print("Name and Last name has been successfully deleted")
        self.first = None
        self.last = None
    
#CREATE INSTANCES NOW
Employee_01 = Employee("Felipe", "Camacho", "Geocientifico", "GIS")
Employee_01.display_information()
Employee_01.fullname = "Andres Hurtado"
Employee_01.display_information()

del Employee_01.fullname
Employee_01.display_information()

