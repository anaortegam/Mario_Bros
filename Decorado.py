#importa las constantes del juego para que se puedan usar en esta clase
import Constantes as c

#Permite crear objetos de tipo Decorado, cuenta con una posición x, una posición y cuenta con la variable tipo dependiendo del tipo de bloque que va a ser
#Es una superclase
class Decorado():
    def __init__(self, x, y, tipo):
        self.__x = x
        self.__y = y
        self.tipo = tipo

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
