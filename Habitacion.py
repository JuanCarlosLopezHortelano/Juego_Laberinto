from Contenedor import Contenedor
from ElementoMapa import ElementoMapa
from Orientacion import Orientacion
from Norte import Norte
from Sur import Sur
from Este import Este
from Oeste import Oeste
from Hoja import Hoja
from Orientacion import Orientacion


class Habitacion(Contenedor):
    def __init__(self, id):

        self.id = id
        self.orientaciones = [Orientacion]
        self.hijos = []
        self.norte
        self.sur
        self.este
        self.oeste

    def entro(self):
        print("Te encuentras en la habitacion ", self.id)

    def norte(self):
        return super().norte()

    def sur(self):
        return super().sur()

    def este(self):
        return super().este()

    def oeste(self):
        return super().oeste()

    def agregar_elemento(self, ElementoMapa):
        super().agregar_elemento(ElementoMapa)

    def añadirOrientacion(self, Orientacion):
        super().añadirOrientacion(Orientacion)

    def ponerEN(self,Orientacion, EM):
        Orientacion.ponerEM(EM,self)


