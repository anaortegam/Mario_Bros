#Permite crear objetos de tipo Enemigos
#Es una superclase

#importa la librería de pyxel y las constantes del programa
import pyxel
import Constantes as c
#En el constructor de la clase se definen las coordenadas de los enemigos, el tipo, su movimiento y si está vivo o no.
class Enemigos():
    def __init__(self, x, y, tipo):
        self.__x = x
        self.__y = y
        self.__tipo = tipo
        self.__aire = True
        self.__dcha = False
        self.__izq = True
        self.__vivo = True

    #estos atributos se crean privados.
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def vivo(self):
        return self.__vivo

    @property
    def tipo(self):
        return self.__tipo

    #Modifica el movimiento de los enemigos en función de si colisionan y en función de la posición de Mario.
    def update(self, x_mario, saltando_dcha):
        #si se salen de la pantalla dejan de estar vivos.
        if self.__x + c.anchura_enemigos < 0 or self.__y > 200:
            self.__vivo = False

        #se mueven a la izquierda con una velocidad determinada.
        #si Mario está en la mitad de la pantalla también se mueve el fondo, por lo que hay que cambiar la velocidad de los enemigos.
        if self.__izq:
            if x_mario + c.anchura_Mario == c.mitad_pantalla and (pyxel.btn(pyxel.KEY_RIGHT) or saltando_dcha):
                self.__x -= c.velocidad_enemigos_x + c.velocidad
            else:
                self.__x -= c.velocidad_enemigos_x

        if self.__dcha:
            if x_mario + c.anchura_Mario == c.mitad_pantalla and (pyxel.btn(pyxel.KEY_RIGHT) or saltando_dcha):
                self.__x += c.velocidad_enemigos_x - c.velocidad
            else:
                self.__x += c.velocidad_enemigos_x

        #si están en el aire tienen que bajar.
        if self.__aire:
            self.__y += c.velocidad_enemigos_y

    # Esta función comprueba si la posicion de un enemigo coincide con algín objeto colisionable.
    # Dependiendo de como colisione se modifican sus atributos.
    def Colisionar(self, colisionables):
        self.__aire = True
        for item in colisionables:
            #enemigo tipo goomba
            if self.tipo == 1:
                #tuberías
                if item.tipo == 5:
                    #cuando un enemigo choca lateralmente con una tubería
                    if item.x + c.anchotuberias - 1 <= self.__x <= item.x + c.anchotuberias + 1  and item.y <= self.__y <= item.y + (c.alto_pantalla - item.y - c.altura_suelo):
                        self.__dcha = True
                        self.__izq = False
                    elif item.x -1 <= self.__x + c.anchura_enemigos <= item.x +1 and item.y <= self.__y <= item.y + (c.alto_pantalla - item.y - c.altura_suelo):
                        self.__izq = True
                        self.__dcha = False
                else:
                    #cuando un enemigo está sobre un bloque
                    if self.y + c.altura_goomba == item.y and item.x - c.anchura_enemigos <= self.x <= item.x + c.tamaño_bloque:
                        self.__aire = False
                    # cuando un enemigo choca lateralmente con un bloque
                    if item.x + c.tamaño_bloque - 1 <= self.__x <= item.x + c.tamaño_bloque + 1  and item.y <= self.__y <= item.y + c.tamaño_bloque:
                        self.__dcha = True
                        self.__izq = False
                    elif item.x -1 <= self.__x + c.anchura_enemigos <= item.x +1 and item.y <= self.__y <= item.y + c.tamaño_bloque:
                        self.__izq = True
                        self.__dcha = False
            #enemigo tipo koopa troopa
            else:
                #tuberías
                if item.tipo == 5:
                    # cuando un enemigo choca lateralmente con una tubería
                    if item.x + c.anchotuberias - 1 <= self.__x <= item.x + c.anchotuberias + 1 and item.y <= self.__y <= item.y + (c.alto_pantalla - item.y - c.altura_suelo):
                        self.__dcha = True
                        self.__izq = False
                    elif item.x - 1 <= self.__x + c.anchura_enemigos <= item.x + 1 and item.y <= self.__y <= item.y + (c.alto_pantalla - item.y - c.altura_suelo):
                        self.__izq = True
                        self.__dcha = False
                else:
                    # cuando un enemigo está sobre un bloque
                    if self.y + c.altura_koopa == item.y and item.x - c.anchura_enemigos <= self.x <= item.x + c.tamaño_bloque:
                        self.__aire = False
                    # cuando un enemigo choca lateralmente con un bloque
                    if item.x + c.tamaño_bloque - 1 <= self.__x <= item.x + c.tamaño_bloque + 1 and item.y <= self.__y <= item.y + c.tamaño_bloque:
                        self.__dcha = True
                        self.__izq = False
                    elif item.x - 1 <= self.__x + c.anchura_enemigos <= item.x + 1 and item.y <= self.__y <= item.y + c.tamaño_bloque:
                        self.__izq = True
                        self.__dcha = False



