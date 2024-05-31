#importa la clase bloque
from Bloque import Bloque

#Permite crear objetos de tipo Bloque_liso
#Hereda las características de la superclase Bloque
class Bloque_liso(Bloque):
    def __init__(self, x, y, tipo):
        super().__init__(x,y, tipo)
        self.tipo = 4
