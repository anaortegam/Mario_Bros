#importa las constantes del juego para que se puedan usar en esta clase
import Constantes as c

#Permite crear objetos de tipo bandera.
#No tiene herencia
class Bandera():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    #sus posiciones son privadas porque no deberían ser modificables desde el exterior.
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    # va actualizando la posición x del objeto
    def update(self):
        self.__x -= c.velocidad