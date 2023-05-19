from Decorator import Decorator


class Fuego(Decorator):
    def __init__(self):

        super().__init__()
    def entro(self):
        super().entro()
        self.componente.entro()
        print("Has entrado en un incendio")