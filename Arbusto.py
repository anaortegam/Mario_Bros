#importa la clase decorada ya que va a ser utiliada en esta clase.

from Decorado import Decorado
#Permite crear objetos de tipo Arbusto
#Hereda las características de la superclase Decorado
class Arbusto(Decorado):
    def __init__(self, x, y, tipo):
        super().__init__(x, y, tipo)
        self.tipo = 1
