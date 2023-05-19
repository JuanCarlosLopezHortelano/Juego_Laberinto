from Hoja import Hoja



class Decorator(Hoja):

    def __init__(self):
        self.componente = None

    def entro(self):
        super().entro()



    def componente(self,EM):
        self.componente = EM

