from Fuego import Fuego
from Juego import Juego


class PlayGround():
     def menu_de_juego(self):

             print("Bienvenido al Menú de Laberintos")
             print("1. Laberinto_Juego con Dos Habitaciones")
             print("2. Laberinto_Juego con 4 Habitaciones")
             print("3. Salir")
             opcion = input("Ingrese su elección (1/2/3): ")

             if opcion == "1":
                 print("Ha seleccionado el Laberinto_Juego con Dos Habitaciones ")
                 print("INACTIVO")
                 self.menu_de_juego()
             elif opcion == "2":
                 print("Ha seleccionado el Laberinto_Juego con 4 Habitaciones")
                 self.juego_laberinto4habitaciones()

             elif opcion == "3":
                 print("Saliendo del programa...")
                 exit()
             else:
                 print("Opción inválida. Por favor, ingrese 1, 2 o 3")
                 self.menu_de_juego()



     def laberinto2habitaciones(self):
         pass

     def juego_laberinto4habitaciones(self):
          juego = Juego()
          laberinto = juego.fabricar_lab4habsFMComposite()
          print("____________________EMPEZANDO EL JUEGO__________________")
          print("\n")
          print("En qué habitación quieres empezar?")
          opcion = input("Habitacion (1/2/3/4): ")

          if opcion == "1":
              print("Ha seleccionado la Habitación 1")
              print("Nos encontramos en la primera habitación")
              print("Hacia qué dirección quieres ir?")
              hab = laberinto.obtenerHabitacion(0)
              elige_direccion = input()
              if elige_direccion == "norte":
                 hab.norte.entro()
              elif elige_direccion == "este":
                  hab.este.entro()
              elif elige_direccion == "oeste":
                  hab.oeste.entro()
              elif elige_direccion == "sur":
                  hab.sur.entro()
              else:
                  print("Dirección incorrecta, opciones válidas: norte, sur, este, oeste")

          elif opcion == "2":
              print("Ha seleccionado la Habitación 2")
              print("Nos encontramos en la primera habitación")
              print("Hacia qué dirección quieres ir?")

              hab = laberinto.obtenerHabitacion(1)
              elige_direccion = input()
              if elige_direccion == "norte":
                  hab.norte.estado.resolver_acertijo()
                  hab.norte.entro()
              elif elige_direccion == "este":
                  hab.este.entro()
              elif elige_direccion == "oeste":
                  hab.oeste.entro()
              elif elige_direccion == "sur":
                  hab.sur.entro()
              else:
                  print("Dirección incorrecta, opciones válidas: norte, sur, este, oeste")
          elif opcion == "3":
              print("Ha seleccionado la Habitación 3")
              print("Nos encontramos en la primera habitación")
              print("Hacia qué dirección quieres ir?")

              hab = laberinto.obtenerHabitacion(2)
              elige_direccion = input()
              if elige_direccion == "norte":
                  hab.norte.entro()
              elif elige_direccion == "este":
                  hab.este.entro()
              elif elige_direccion == "oeste":
                  hab.oeste.entro()
              elif elige_direccion == "sur":
                  hab.sur.entro()
              else:
                  print("Dirección incorrecta, opciones válidas: norte, sur, este, oeste")
          elif opcion == "4":
              print("Ha seleccionado la Habitación 4")

              print("Nos encontramos en la primera habitación")

              hab = laberinto.obtenerHabitacion(3)
              Fuego(hab).entro()
              print("Hacia qué dirección quieres ir?")
              elige_direccion = input()
              if elige_direccion == "norte":
                  hab.norte.entro()
              elif elige_direccion == "este":
                  hab.este.entro()
              elif elige_direccion == "oeste":
                  hab.oeste.entro()
              elif elige_direccion == "sur":
                  hab.sur.entro()
              else:
                  print("Dirección incorrecta, opciones válidas: norte, sur, este, oeste")
          else:
              print("Opción inválida. Por favor, ingrese 1, 2, 3 o 4")






