from ElementoMapa import ElementoMapa
from abc import ABC, abstractmethod
class Hoja(ElementoMapa,ABC):

    def entro(self):
        print("Entrando a....")