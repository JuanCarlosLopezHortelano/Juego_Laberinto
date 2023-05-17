from Bomba import Bomba
from BombaActivadaState import BombaActivadaState
from Juego import Juego
from Pared import Pared
from PlayGround import PlayGround

if __name__ == '__main__':

 #bomba = Bomba(Pared())

 #bomba.cambiar_estado(BombaActivadaState(bomba))
 #bomba.estado.resolver_acertijo()  # Si la respuesta es correcta, la salida será: ¡Acertaste el acertijo! La bomba se desactiva.
 #bomba.entro()
 partida = PlayGround()
 partida.menu_de_juego()

 #juego = Juego()
 #laberinto = juego.fabricar_lab2habsFM()
 #hab= laberinto.obtenerHabitacion(0)
 #hab.norte.entro()