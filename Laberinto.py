class Laberinto():
    def __init__(self):
        self.habitaciones = []

    def habitaciones(self):
        return self.habitaciones

    def añadir_habitacion(self, nueva_habitacion):
        self.habitaciones.append(nueva_habitacion)

    def obtenerHabitacion(self, id):
        return self.habitaciones[id]


