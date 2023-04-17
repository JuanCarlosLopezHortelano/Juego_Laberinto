
from Laberinto import Laberinto
from Habitacion import Habitacion
from Pared import Pared
from main import Bicho
from Puerta import Puerta
class Juego():

    def __init__(self):
        self.laberinto

    def laberinto(self):
        return self.laberinto

    def fabricar_laberinto(self):
        return Laberinto()

    def fabricar_habitacion(self, id):
        habitacion = Habitacion(id)
        habitacion.norte = self.fabricarPared()
        habitacion.sur = self.fabricarPared()
        habitacion.este = self.fabricarPared()
        habitacion.oeste = self.fabricarPared()
        return habitacion

    def fabricar_bomba(self):
        pass

    def fabricar_puerta(self, lado1, lado2, abierta):
        puerta = Puerta(lado1, lado2, abierta)
        return puerta

    def fabricarPared(self):
        return Pared()

    def fabricar_bicho(self, modo, posicion):
        return Bicho(self, modo, posicion)

    def añadir_bicho(self, bicho):
        self.bichos.append(bicho)

    def juego_2habsFM(self):
        habitacion1 = self.fabricar_habitacion(1)
        habitacion1.oeste
        habitacion1.este
        habitacion1.sur

        habitacion2 = self.fabricar_habitacion(2)
        habitacion2.oeste
        habitacion2.este
        habitacion2.norte

        puerta = self.fabricar_puerta(habitacion1, habitacion2, 'true')
        habitacion1.norte = puerta
        habitacion2.sur = puerta

        laberinto = self.fabricar_laberinto()
        laberinto.añadir_habitacion(habitacion1)
        laberinto.añadir_habitacion(habitacion2)
        print("____________________EMPEZANDO EL JUEGO__________________")
        print("\n")
        print("En qué habitación quieres empezar?")
        elige_habitacion = None

        while elige_habitacion != "3":
            elige_habitacion = input("Habitacion: ")

            if elige_habitacion == "1":
                print("Nos encontramos en la primera habitación")
                print("Hacia qué dirección quieres ir?")

                elige_direccion = input()
                if elige_direccion == "norte":
                    habitacion1.norte.entro()
                elif elige_direccion == "este":
                    habitacion1.este.entro()
                elif elige_direccion == "oeste":
                    habitacion1.oeste.entro()
                elif elige_direccion == "sur":
                    habitacion1.sur.entro()
                else:
                    print("Dirección incorrecta, opciones válidas: norte, sur, este, oeste")

            elif elige_habitacion == "2":
                print("Nos encontramos en la segunda habitación")
                print("Hacia qué dirección quieres ir?")

                elige_direccion = input()
                if elige_direccion == "norte":
                    habitacion2.norte.entro()
                elif elige_direccion == "este":
                    habitacion2.este.entro()
                elif elige_direccion == "oeste":
                    habitacion2.oeste.entro()
                elif elige_direccion == "sur":
                    habitacion2.sur.entro()
                else:
                    print("Dirección incorrecta, opciones válidas: norte, sur, este, oeste")

            elif elige_habitacion == "3":
                print("Saliendo del laberinto...")

            else:
                print("Elige una habitación correcta. Las opciones son 1 y 2. Ingresa 3 para salir del laberinto.")

        print("Fin del laberinto.")
        return laberinto