# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:00:42 2021

@author: ferna
"""
#Ambas líneas permiten importar la librería de pyxel y el archivo de constantes
import pyxel
import Constantes as c

#Esta clase permite crear objetos tipo Mario
#No tiene herencia

class Mario():

    #En el constructor de esta clase se llama a la función reset que establece los parámetros iniciales de Mario.
    #También tiene dos atributos que son sus vidad y si está vivo.
    def __init__(self, vidas):
        self.__reset()
        self.__vidas = vidas
        self.__vivo = True

    #Muchos de los atributos de Mario están privados por lo que hay que usar métodos property
    #para que puedan ser leídos y usados en otras clases.
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def vidas(self):
        return self.__vidas

    @property
    def saltando_dcha(self):
        return self.__saltando_dcha

    @property
    def saltando_izq(self):
        return self.__saltando_izq

    @property
    def vivo(self):
        return self.__vivo

    #La función reset establece los parámetros iniciales de Mario.
    #Al principio Mario no está saltando y está en el aire hasta que colisione con algún bloque.
    def __reset(self):
        self.__y = c.posicion_inicialY
        self.__x = c.posicion_inicialX
        self.__aire = True
        self.__saltando = False
        self.__saltando_izq = False
        self.__saltando_dcha = False

    #Tomando los valores de algunos atributos, permite mover al objeto de dicho tipo por pantalla
    #Dependiendo de que se introduzca por teclado cambian las propiedades de Mario y se mueve de distintas formas.

    def Mover(self, bandera):

        #Si Mario llega a la posición de la bandera gana y ya no es controlado por el jugadora.
        #Se mueve automáticamente hacia la izquierda.
        if self.__x >= bandera:
            self.__x += c.velocidad_Mario_x

        #Si Mario no está en la bandera se mueve con las siguientes condiciones.
        else:
            if not self.__saltando_izq:
                if pyxel.btn(pyxel.KEY_LEFT):
                    #Mario no puede retroceder hacia atrás en el nivel.
                    self.__x = max(self.__x - c.velocidad_Mario_x, 0)

            if not self.__saltando_dcha:
                if pyxel.btn(pyxel.KEY_RIGHT):
                    #Mario no puede pasar de la mitad de la pantalla.
                    self.__x = min(self.__x + c.velocidad_Mario_x, c.mitad_pantalla-c.anchura_Mario)

            #Con estas condiciones establecemos que si Mario si está moviendo hacia el lado y salta realice el salto completo hacia ese lado
            if pyxel.btn(pyxel.KEY_LEFT):
                if pyxel.btn(pyxel.KEY_UP):
                    self.__saltando_izq = True

            if pyxel.btn(pyxel.KEY_RIGHT):
                if pyxel.btn(pyxel.KEY_UP):
                    self.__saltando_dcha = True

            #resetea los atributos que intervienen en el salto cuando este termina
            if c.variacion_y == 0 or not self.__aire:
                self.__saltando = False
                #self.__aire = False
                c.velocidad_Mario_y = 11
                c.variacion_y = 0
                self.__saltando_izq = False
                self.__saltando_dcha = False

            #solo puede saltar si no está saltando y no está en el aire, es decir, si está en un bloque.
            if pyxel.btn(pyxel.KEY_UP) and not self.__saltando and not self.__aire:
                self.__saltando = True
            if self.__saltando:
                self.__aire = True
                #si está saltando hacia la izquierda o la derecha, también cambiará la x de Mario
                if self.__saltando_izq:
                    self.__x = max(self.__x - c.velocidad_salto_x, 0)
                if self.__saltando_dcha:
                    self.__x = min(self.__x + c.velocidad_salto_x, c.mitad_pantalla - c.anchura_Mario)
                self.__y -= c.velocidad_Mario_y
                c.variacion_y += c.velocidad_Mario_y
                c.velocidad_Mario_y -= 1

            if self.__aire and not self.__saltando:
                self.__y += 5

            if self.__y > 200:
                self.__vidas -=1
                self.__reset()

            if self.__vidas == 0:
                self.__vivo = False

    #Esta función comprueba si la posicion de Mario coincide con algín objeto colisionable.
    #Dependiendo de como colisione se modifican sus atributos.
    def Colisionar(self, colisionables):
        self.__aire = True
        c.velocidad_Mario_x = 2
        c.velocidad_salto_x = 2
        c.velocidad = 2
        for item in colisionables:
            #se hace una diferencia entre las tuberías y el resto de bloques ya que tienen distintas dimensiones
            if item.tipo == 5:
                #Mario está encima de una tubería.
                if item.y - 3 <= self.y + c.altura_Mario <= item.y + 3 and item.x - c.anchura_Mario< self.x < item.x + c.anchotuberias:
                    self.__aire = False
                    self.__y = item.y - c.altura_Mario
                #Mario choca con una tubería por la derecha.
                elif self.__x + c.anchura_Mario - 2 <= item.x<= self.__x + c.anchura_Mario + 2  and item.y <= self.__y <= item.y + (c.alto_pantalla - item.y - c.altura_suelo):
                    self.__saltando_dcha = False
                    if pyxel.btn(pyxel.KEY_RIGHT):
                        if self.__x == 115:
                            c.velocidad = 0
                        else:
                            c.velocidad_Mario_x = 0
                # Mario choca con una tubería por la izquierda.
                elif self.__x - 1 <= item.x + c.anchotuberias<= self.__x +1 and item.y <= self.__y <= item.y + (c.alto_pantalla - item.y - c.altura_suelo):
                    self.__saltando_izq = False
                    if pyxel.btn(pyxel.KEY_LEFT):
                        c.velocidad_Mario_x = 0
            else:
                # Mario está encima de un bloque.
                if item.y - 5 <= self.y + c.altura_Mario <= item.y + 5 and item.x - c.anchura_Mario <= self.x <= item.x + c.tamaño_bloque:
                    self.__aire = False
                    self.__y = item.y - c.altura_Mario
                # Mario salta y choca con un bloque
                elif item.y + c.tamaño_bloque - 3 <= self.y <= item.y + c.tamaño_bloque + 3 and item.x - c.anchura_Mario <= self.x <= item.x + c.tamaño_bloque:
                    self.__saltando = False
                    self.__aire = True
                    c.variacion_y = 0
                # Mario choca con un bloque por la derecha.
                if item.x -2 <= self.__x + c.anchura_Mario <= item.x +2 and item.y<= self.__y<= item.y + c.tamaño_bloque:
                    self.__saltando_dcha = False
                    if pyxel.btn(pyxel.KEY_RIGHT):
                        if self.__x == 115:
                            c.velocidad = 0
                        else:
                            c.velocidad_Mario_x = 0
                # Mario choca con un bloque por la izquierda.
                if  item.x -2 <= self.__x - c.anchura_Mario <= item.x +2 and item.y<= self.__y<= item.y + c.tamaño_bloque:
                    if pyxel.btn(pyxel.KEY_LEFT):
                        c.velocidad_Mario_x = 0



