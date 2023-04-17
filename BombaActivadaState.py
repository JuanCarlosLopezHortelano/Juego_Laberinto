from BombaState import BombaState


class BombaActivadaState(BombaState):
    def __init__(self, EM):
        self.componente = EM
        self.acertijo_resuelto = False

    def entro(self):
        super().entro()
        self.componente.entro()
        print("Había una BOMBAA!!")

    def resolver_acertijo(self):
        print("Resuelve el acertijooo")
        respuesta = input("Mas vale pajaro en mano que ")
        if respuesta == "cuchara de palo":
            print("¡Acertaste el acertijo! La bomba se desactiva.")
            self.acertijo_resuelto = True
        else:
            print("Respuesta incorrecta. La bomba sigue activada.")

        if self.acertijo_resuelto:
           self.bomba.desactivar_bomba()