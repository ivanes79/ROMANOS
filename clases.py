class Heroe:
    #nombre,poder,apodo son variables de la clase Heroe
    #nombre,poder,apodo son atributos de la clase Heroe
    nombre=""
    poder=""
    apodo=""
    edad=40
    #funcion que inicializa la clase heroe
    #self valor inicial que indica para atributos y
    #  funciones que pertenecen a la misma clase
    #se le llama constructor de la clase Heroe
    def __init__(self,nombre,poder,apodo):
       self.nombre=nombre
       self.poder=poder
       self.apodo=apodo

    def saludar(self):
        print("hola como vamos, "+self.nombre)

    def datos_heroe(self):
        return f"Heroe: nombre: {self.nombre}, poder:{self.poder}, apodo:{self.apodo}"
    #metodo magico devolver como cadena representacion de atributos del objeto
    def __str__(self) -> str:
        return f"Heroe: nombre: {self.nombre}, poder:{self.poder}, apodo:{self.apodo}"
    #metodo magico para representar una cadena de devolucion final
    def __repr__(self) -> str:
        return f"Heroe: nombre: {self.nombre}, poder:{self.poder}, apodo:{self.apodo}"

#spiderman es objeto de la clase Heroe
#spiderman es una instancia de la clase Heroe
spiderman = Heroe("Peter Parker","super fuerza","Spiderman")
spiderman.edad=60 
print( str(spiderman) )
"""
spiderman.nombre="Peter Parker"
spiderman.poder="super fuerza"
spiderman.apodo="Spiderman" 
"""

ironman=Heroe("Tony Stark","Millonario","Hombre de acero")
"""
ironman.nombre="Tony Stark"
ironman.poder="Millonario"
ironman.apodo="Hombre de acero"
"""
print(spiderman.nombre)
print(ironman.nombre)