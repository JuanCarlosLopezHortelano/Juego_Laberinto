from Decorator import Decorator
from BombaDesactivadaState import BombaDesactivadaState
class Bomba(Decorator):
    def __init__(self):
        self.estado = BombaDesactivadaState()
        self.estado.bomba = self

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def entro(self):
        self.componente.entro()
        print("Hay algo")
        self.estado.entro()

    def desactivar_bomba(self):
        self.cambiar_estado(BombaDesactivadaState())
        print("La bomba ha sido desactivada.")