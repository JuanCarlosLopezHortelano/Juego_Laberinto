from ElementoMapa import ElementoMapa
class Habitacion(ElementoMapa):
    def __init__(self, id):
        self.norte
        self.sur
        self.este
        self.oeste
        self.id = id

    def norte(self):
        return self.norte

    def sur(self):
        return self.sur

    def este(self):
        return self.este

    def oeste(self):
        return self.oeste

    def entro(self):
        print("Te encuentras en la habitacion ", self.id)
