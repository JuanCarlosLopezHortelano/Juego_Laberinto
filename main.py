# This is a sample Python script.


## STRATEGY
#La implementacion de este patron en el Laberinto_Juego se hace a traves de
#la clase Modo y las clases Agresivo y Perezoso que definen
#la estrategia o funciones de la clase Bicho( contexto) que dependiendo
#del modo que enga actuara de forma distina
#DE MOMENTO OMITIMOS ARIBUTOS COMO VIDA Y PODER
class Bicho():

    def __init__(self, id, modo, posicion, poder, vidas):
        self.id = id
        self.modo = modo
        self.posicion = posicion
        self.poder = poder
        self.vidas = vidas

    def esAgresivo(self):
        return self.modo.esAgresivo()

    def esPerezoso(self):
        return self.modo.esPerezoso()

    def setModo(self, modo):
        self.modo = modo
from abc import ABC, abstractmethod

class Modo(ABC):
    def esAgresivo(self):
      return False
    def esPerezoso(self):
      return False


class Agresivo(Modo):

    def esAgresivo(self):
        return True

    def esPerezoso(self):
        return False

    def __str__(self):
        return "Este bicho es Agresivo"


class Perezoso(Modo):

    def esAgresivo(self):
        return False

    def esPerezoso(self):
        return True

    def __str__(self):
        return "Este bicho es Perezoso"




#PRUEBA CREAR BICHOS


# Creamos un bicho normal
bicho_normal = Bicho("1", Modo(),None,None,None)

# Probamos los métodos de un bicho normal
print(bicho_normal.esAgresivo())  # Imprime: False
print(bicho_normal.esPerezoso())  # Imprime: False

# Cambiamos el modo a agresivo
bicho_normal.setModo(Agresivo())

# Probamos los métodos de un bicho agresivo
print(bicho_normal.esAgresivo())  # Imprime: True
print(bicho_normal.esPerezoso())  # Imprime: False

# Cambiamos el modo a perezoso
bicho_normal.setModo(Perezoso())

# Probamos los métodos de un bicho perezoso
print(bicho_normal.esAgresivo())  # Imprime: False
print(bicho_normal.esPerezoso())  # Imprime: True






