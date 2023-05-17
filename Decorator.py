from Hoja import Hoja



class Decorator(Hoja):

    def __init__(self, EM):
        self.componente = EM
    def entro(self):
        super().entro()


