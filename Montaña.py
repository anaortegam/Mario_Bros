#importa la clase decorado
from Decorado import Decorado

#Permite crear objetos de tipo Montaña
#Hereda las características de la superclase Decorado
class Montaña(Decorado):
    def __init__(self, x, y, tipo):
        super().__init__(x, y, tipo)
        self.tipo = 3