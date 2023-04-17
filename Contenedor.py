from ElementoMapa import ElementoMapa
from Orientacion import Orientacion



from ElementoMapa import ElementoMapa
from Orientacion import Orientacion
from Norte import Norte
from Sur import Sur
from Este import Este
from Oeste import Oeste
from Hoja import Hoja
class Contenedor(ElementoMapa):

    def __init__(self):
        self.orientaciones = [Orientacion]
        self.hijos =  []
        self.norte
        self.sur
        self.este
        self.oeste

    def norte(self):
        return self.norte

    def sur(self):
        return self.sur

    def este(self):
        return self.este

    def oeste(self):
        return self.oeste
    def agregar_elemento(self,ElementoMapa):
        self.hijos.append(ElementoMapa)

    def añadirOrientacion(self,Orientacion):
        self.orientaciones.append(Orientacion)

    def ponerEN(self, Orientacion, EM):
        Orientacion.ponerEM(EM, self)