#importa la clase decorado
from Decorado import Decorado

#Permite crear objetos de tipo Catillo
#Hereda las características de la superclase Decorado
class Castillo(Decorado):
    def __init__(self, x, y, tipo):
        super().__init__(x, y, tipo)
        self.tipo = 2