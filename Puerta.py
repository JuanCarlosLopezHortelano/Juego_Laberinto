from ElementoMapa import ElementoMapa
class Puerta(ElementoMapa):
  # bool abierta
  def __init__ (self,lado1,lado2,abierta):
      self.lado1 = lado1
      self.lado2 = lado2
      self.abierta = abierta
  def entro(self):
      if self.abierta :
          print("Esta abierta")
      else:
          print("Esta cerrado")
