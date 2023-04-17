from Decorator import Decorator


class Espada(Decorator):
    def __init__(self,EM):

        self.componente = EM
    def entro(self):
        super().entro()
        self.componente.entro()
        print("HAS ENCONTRADO UNA ESPADA")