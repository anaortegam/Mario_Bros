
#importa la clase bloque
from Bloque import Bloque

#Permite crear objetos de tipo Bloque_ladrillo_rompible
#Hereda las características de la superclase Bloque
class Bloque_ladrillo_rompible(Bloque):
    def __init__(self, x, y, tipo):
        super().__init__(x, y, tipo)
        self.tipo = 3
