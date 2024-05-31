#importa la clase enemigos
from Enemigos import Enemigos

#Permite crear objetos de tipo Goomba
#Hereda las características de la superclase Enemigos
class Koopa(Enemigos):
    def __init__(self, x, y, tipo):
        super().__init__(x,y, tipo)
        self.tipo = 2