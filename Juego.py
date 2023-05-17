from Bomba import Bomba
from BombaActivadaState import BombaActivadaState
from Cofre import Cofre
from Espada import Espada
from Este import Este
from Fuego import Fuego
from Laberinto import Laberinto
from Habitacion import Habitacion
from Norte import Norte
from Oeste import Oeste
from Pared import Pared
from Sur import Sur
from main import Bicho
from Puerta import Puerta
from Decorator import Decorator
from BombaDesactivadaState import BombaDesactivadaState

class Juego():

    def __init__(self):
        self.laberinto = None

    def laberinto(self):
        return self.laberinto

    def fabricar_laberinto(self):
     return Laberinto()

    def fabricar_habitacion(self, id):
        habitacion = Habitacion(id)
        habitacion.norte = self.fabricarPared()
        habitacion.sur = self.fabricarPared()
        habitacion.este = self.fabricarPared()
        habitacion.oeste = self.fabricarPared()
        return habitacion

    def fabricar_bomba(self, EM):
        bomba = Bomba(EM)
        return bomba
    def fabricar_puerta(self, lado1, lado2, abierta):
        puerta = Puerta(lado1, lado2, abierta)
        return puerta

    def fabricarPared(self):
        return Pared()

    def fabricar_bicho(self, modo, posicion):
        return Bicho(self, modo, posicion)

    def fabricar_cofre(self):
        return Cofre()

    def añadir_bicho(self, bicho):
        self.bichos.append(bicho)

    def fabricar_HabitacionComposite(self, id):
        hab = Habitacion(id)
        hab.ponerEN(self.fabricarNorte(), self.fabricarPared())
        hab.ponerEN(self.fabricarSur(), self.fabricarPared())
        hab.ponerEN(self.fabricarEste(), self.fabricarPared())
        hab.ponerEN(self.fabricarOeste(), self.fabricarPared())
        return hab

    def fabricarNorte(self):
        return Norte()

    def fabricarSur(self):
        return Sur()

    def fabricarEste(self):
        return Este()

    def fabricarOeste(self):
        return Oeste()

    def fabricar_lab2habsFM(self):
        habitacion1 = self.fabricar_habitacion(1)

        habitacion2 = self.fabricar_habitacion(2)

        puerta = self.fabricar_puerta(habitacion1, habitacion2, True)
        habitacion1.norte = puerta
        habitacion2.sur = puerta

        laberinto = self.fabricar_laberinto()
        laberinto.añadir_habitacion(habitacion1)
        laberinto.añadir_habitacion(habitacion2)
        return laberinto

    def fabricar_lab4habsFMComposite(self):

        hab1 = self.fabricar_HabitacionComposite(1)
        hab2 = self.fabricar_HabitacionComposite(2)
        hab3 = self.fabricar_HabitacionComposite(3)
        hab4 = self.fabricar_HabitacionComposite(4)

        fuego = Fuego(hab4)
        puerta1 = self.fabricar_puerta(hab1, hab2, True)
        puerta2 = self.fabricar_puerta(hab2, hab4, True)
        puerta3 = self.fabricar_puerta(hab4, hab3, True)
        puerta4 = self.fabricar_puerta(hab4, hab1, False)

        espada = Espada(self.fabricar_cofre())

        hab1.ponerEN(self.fabricarEste(), puerta1)
        hab1.ponerEN(self.fabricarSur(), puerta4)
        hab2.ponerEN(self.fabricarOeste(), puerta1)
        hab2.ponerEN(self.fabricarSur(), puerta2)
        hab3.ponerEN(self.fabricarNorte(), puerta4)
        hab3.ponerEN(self.fabricarSur(), espada)
        hab4.ponerEN(self.fabricarNorte(), puerta2)

        bomba = self.fabricar_bomba(self.fabricar_cofre())
        bomba.cambiar_estado(BombaActivadaState(bomba))

        hab2.ponerEN(self.fabricarNorte(), bomba)

        bomba2 = self.fabricar_bomba(puerta3)
        bomba2.cambiar_estado(BombaActivadaState(bomba2))
        hab3.ponerEN(self.fabricarEste(), bomba2)
        hab4.ponerEN(self.fabricarOeste(), bomba2)

        lab = self.fabricar_laberinto()
        lab.añadir_habitacion(hab1)
        lab.añadir_habitacion(hab2)
        lab.añadir_habitacion(hab3)
        lab.añadir_habitacion(hab4)

        return lab
