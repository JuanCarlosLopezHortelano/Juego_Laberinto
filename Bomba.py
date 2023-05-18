
from Decorator import Decorator
from BombaDesactivadaState import BombaDesactivadaState


class Bomba(Decorator):
    def __init__(self, EM):
        super().__init__(EM)
        self.estado = BombaDesactivadaState()

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        self.estado.bomba = self
    def entro(self):
        self.estado.entro()

    def desactivar_bomba(self):
        self.cambiar_estado(BombaDesactivadaState())
        print("La bomba ha sido desactivada")
