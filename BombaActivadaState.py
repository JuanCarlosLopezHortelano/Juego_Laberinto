from BombaState import BombaState
class BombaActivadaState(BombaState):
    def __init__(self, bomba):
        self.bomba = bomba


    def entro(self):
        print("Había una BOMBA!!")
        self.resolver_acertijo()

    def resolver_acertijo(self):
        print("Resuelve el acertijo:")
        respuesta = input("¿Mas vale pájaro en mano que...? ")
        if respuesta == "cuchara de palo":
            print("¡Acertaste el acertijo! La bomba se desactiva.")
            self.bomba.desactivar_bomba()
        else:
            print("Respuesta incorrecta. La bomba sigue activada.")
            print("LA BOMBA EXPLOTO")