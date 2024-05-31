#Ambas líneas permiten importar las librerias de pyxel y random, de manera que podemos usar funciones cuyo comportamiento está encapsulado
import random
import pyxel

#importa las clases que va a necesitar usar Juego
from Bloque import Bloque
import Constantes as c
from Mario import Mario
from Montaña import Montaña
from Arbusto import Arbusto
from Nubes import Nube
from Enemigos import Enemigos
from Castillo import Castillo
from Bandera import Bandera

#Permite iniciar el juego
#No tiene herencia

class Juego():
    #Llama al constructor de la clase y nos permite crear los atributos de todos los objetos de tipo Juego
    #Tiene atributos que necesita el juego para funcionar.
    #realiza los tres comandos que necesita pyxel para ejecutarse.
    def __init__(self):
        # Los dos primeros números hacen referencia al alto y ancho de la pantalla.
        # Los fps son los frames actualizados en un segundo(las veces que se realiza el bucle de update,draw).
        pyxel.init(c.ancho_pantalla, c.alto_pantalla, caption="Mario Bros", fps = c.n_frames)

        pyxel.load("assets/mario_assets.pyxres")

        self.__bloques = self.__CrearBloques()
        self.__enemigos = []
        self.__colisionables = self.__CrearColisionables()
        self.__mario = Mario (3)
        self.__decorado = (Nube(180, 50, 4), Nube(400, 100, 4),Nube(665, 40, 4), Nube(810, 40, 4), Montaña(0, 144, 3), Montaña(350, 144, 3),Arbusto(194, 162, 1), Arbusto(668, 162,1), Castillo(1434, 84,2))
        self.__bandera = Bandera(1370, 10)
        self.__cuenta_atras = c.duracion_juego

        #Esta línea de código llama a las dos funciones update y draw en un bucle infinito, permitiendo que se cumpla
        #lo que esté desarrollado en ellas
        pyxel.run(self.update, self.draw)

    @property
    def colisionables(self):
        return self.__colisionables

    #El temporizador del juego. Comienza en 300 y disminuye 1 cada segundo.
    def __CuentaAtras(self):
        if pyxel.frame_count % 30 == 0:
            self.__cuenta_atras-=1


#Es una función que crea los bloques del nivel como una lista cuyos elementos son objetos que heredan de la clase Bloque
#Como el nivel no cambia las posiciones de los bloques las hemos puesto fijas
    def __CrearBloques(self):
        bloques = []
        # crea el suelo con un agujero de dos bloques
        for i in range(70):
            item = Bloque(c.anchura_suelo * i, c.alto_pantalla - c.altura_suelo, 6)
            bloques.append(item)
        for i in range(72, c.n_bloques):
            item = Bloque(c.anchura_suelo * i, c.alto_pantalla - c.altura_suelo, 6)
            bloques.append(item)
        #bloque individual
        item = Bloque(276, c.altura_1, 1)
        bloques.append(item)
        for i in range(5):#Es un bucle que genera cinco bloques seguidos, teniendo en cuenta su tipo
            if i % 2 == 0:
                item = Bloque(344+ i*c.tamaño_bloque, c.altura_1, 3)
            else:
                item = Bloque(344+ i*c.tamaño_bloque, c.altura_1, 1)
            bloques.append(item)
        # bloques individuales
        item = Bloque(378, c.altura_2, 1)
        bloques.append(item)
        item = Bloque(511, 144, 5)
        bloques.append(item)
        item = Bloque(621, 129, 5)
        bloques.append(item)
        for i in range(5): #Es un bucle que genera cinco bloques seguidos, teniendo en cuenta su tipo
            if i % 2 ==0:
                item = Bloque(732 + i * c.tamaño_bloque, c.altura_1, 2)
            else:
                item = Bloque(732 + i * c.tamaño_bloque, c.altura_1, 1)
            bloques.append(item)
        #crean bloques en grupos de 3 o 4.
        for i in range(3):
            if i ==0:
                item = Bloque(796 + i * c.tamaño_bloque, c.altura_2, 1)
            else:
                item = Bloque(796 + i * c.tamaño_bloque, c.altura_2, 3)
            bloques.append(item)
        for i in range(3):
            if i ==2:
                item = Bloque(876 + i * c.tamaño_bloque, c.altura_2, 1)
            else:
                item = Bloque(876 + i * c.tamaño_bloque, c.altura_2, 3)
            bloques.append(item)
        for i in range(4):
            if i==0:
                item = Bloque(908 + i * c.tamaño_bloque, c.altura_1, 3)
            elif i==2:
                item = Bloque(908 + i * c.tamaño_bloque, c.altura_1, 1)
            else:
                item = Bloque(908 + i * c.tamaño_bloque, c.altura_1, 2)
            bloques.append(item)
        item = Bloque(1020, 129, 5)
        bloques.append(item)
        #crea los bloques en escalera.
        for i in range(4):
            item = Bloque(1260 + i * c.tamaño_bloque, c.alto_pantalla - c.altura_suelo - c.tamaño_bloque, 7)
            bloques.append(item)
        for i in range(3):
            item = Bloque(1276 + i * c.tamaño_bloque, c.alto_pantalla - c.altura_suelo - 2 * c.tamaño_bloque, 7)
            bloques.append(item)
        for i in range(2):
            item = Bloque(1292 + i * c.tamaño_bloque, c.alto_pantalla - c.altura_suelo - 3 * c.tamaño_bloque, 7)
            bloques.append(item)
        item = Bloque(1292 + i * c.tamaño_bloque, c.alto_pantalla - c.altura_suelo - 4 * c.tamaño_bloque, 7)
        bloques.append(item)
        return bloques

#Es una función que crea a los enemigos, teniendo en cuenta que los Goomba aparaecen con un 75% de probabilidad y los Koopa un 25%
#Se utiliza el contador de frames de pyxel para que se generen durante un tiempo determinado los enemigos
#crea una lista con todos los enemigos
    def __CrearEnemigos(self):
        tipo = random.randint(1, 4)
        if len(self.__enemigos) < 4: #No más de cuatro enemigos podrán ser generados
            if pyxel.frame_count % 150 == 0: #se generarán enemigos cada 5 segundos
                if tipo == 1:
                    item = Enemigos(random.randint(c.ancho_pantalla, c.longitud_juego-c.ancho_pantalla), 151, 2) #Tienen posiciones aleatorias
                    self.__enemigos.append(item)
                else:
                    item = Enemigos(random.randint(c.ancho_pantalla, c.longitud_juego-c.ancho_pantalla), 161, 1)
                    self.__enemigos.append(item)

#Crea todos los objetos con los que Mario colisiona
    def __CrearColisionables(self):
        colisionables = []
        for item in self.__bloques:
            colisionables.append(item)
        return colisionables


# Esta función es la encargada de decir si el jugador gana la partida
# En caso de cumplirse las condiciones, se cierra la aplicación
    def __GanarPartida(self):
        if self.__mario.x >= 213:
            pyxel.quit()

# Esta función es la encargada de decir si el jugador pierde la partida
# En caso de cumplirse las condiciones, se cierra la aplicación
    def __PerderPartida(self):
        if self.__mario.vivo == False:
            pyxel.quit()

 # Función encargada de actualizar todos los métodos a los que se haga referencia en ell
    def update(self):

        if pyxel.btnp(pyxel.KEY_Q):     #Presionando la Q se abandona el juego
            pyxel.quit()

        self.__PerderPartida()
        self.__GanarPartida()

        self.__CuentaAtras()
        self.__mario.Colisionar(self.colisionables)  # Le establece a Mario todos los objetos con los que colisiona
        self.__mario.Mover(self.__bandera.x)         # El movimiento de Mario cambia cuando llega a la bandera, por lo que la función Mover de Mario necesita saber donde está la bandera
        self.__CrearEnemigos()                       #Llamamos a la función enemigos


        #Si Mario está en el centro de la pantalla, actualiza la posición de los bloques
        if self.__mario.x == c.mitad_pantalla - c.anchura_Mario and (pyxel.btn(pyxel.KEY_RIGHT) or self.__mario.saltando_dcha):
            for item in self.__bloques:
                item.update()

        #Si Mario está en el centro de la pantalla, actualiza la posición del decorado
        if self.__mario.x == c.mitad_pantalla - c.anchura_Mario and (pyxel.btn(pyxel.KEY_RIGHT) or self.__mario.saltando_dcha):
            for item in self.__decorado:
                item.update()

        #Si Mario está en el centro de la pantalla, actualiza la posición de la bandera
        if self.__mario.x == c.mitad_pantalla - c.anchura_Mario and (pyxel.btn(pyxel.KEY_RIGHT) or self.__mario.saltando_dcha):
            self.__bandera.update()

        for item in self.__enemigos:
            item.Colisionar(self.colisionables)
            item.update(self.__mario.x, self.__mario.saltando_dcha)    #Permite que se actualice la posición de los enemigos
            if item.vivo == False:                                     #En caso de que el enemigo sea eliminado o desaparezaca de pantalla, dejará de estar vivo
                self.__enemigos.remove(item)                           #Se elimina de la lista de enemigos porque deja de existir

    # Función encargada de dibujar a todos todos los métodos que se nombran en ella
    # Trabaja conjuntamente con la función update y utiliza la función pyxel.blt para dibujar en una posición X e Y de la pantalla
    # una imagen de un alto u ancho determinadas sacada de un banco de imágenes
    def draw(self):
        #establece el color del fondo del juego
        pyxel.cls(12)

        #dibuja el decorado
        for item in self.__decorado:
            if item.tipo==1:                                   #Según el tipo de decorado que sea, dibujará una cosa u otra
                if 0 <= item.x + 62 <= c.ancho_pantalla + 62:  #Sólo se dibujará en caso de que esté dentro de la pantalla, y se eliminará poco a poco mientras que Mario se mueve
                    pyxel.blt(item.x, item.y, 0, 139, 46, 62, 15)
            elif item.tipo==2:
                if 0 <= item.x + 80 <= c.ancho_pantalla + 80:
                    pyxel.blt(item.x, item.y, 0, 150, 134, 80, 93)
            elif item.tipo==3:
                if 0 <= item.x + 74 <= c.ancho_pantalla + 74:
                    pyxel.blt(item.x, item.y, 0, 0, 193, 74, 33, 7)
            else:
                if 0 <= item.x+45 <= c.ancho_pantalla+45:
                    pyxel.blt(item.x, item.y, 0, 109, 138, 45, 21)

        #dibuja la bandera
        if 0 <= self.__bandera.x + 16 <= c.ancho_pantalla + 16:   #Sólo se dibujará en caso de que esté dentro de la pantalla, y se eliminará poco a poco mientras que Mario se mueve
            pyxel.blt(self.__bandera.x, self.__bandera.y, 0, 226, 59, 22, 167)

        #dibuja los elementos de la lista Bloques dependiendo de que tipo de bloque son.
        for item in self.__bloques:
            if 0 <= item.x + c.tamaño_bloque <= c.ancho_pantalla + c.tamaño_bloque:
                if item.tipo == 1:
                    pyxel.blt(item.x, item.y, 0, 177, 27, c.tamaño_bloque, c.tamaño_bloque)
                elif item.tipo ==2 or item.tipo == 3:
                    pyxel.blt(item.x, item.y, 0, 89, 163, c.tamaño_bloque, c.tamaño_bloque)
                elif item.tipo == 6:
                    pyxel.blt(item.x, item.y, 0, 0, 227, c.tamaño_bloque, c.altura_suelo)
                elif item.tipo == 7:
                    pyxel.blt(item.x, item.y, 0, 0, 62, c.tamaño_bloque, c.tamaño_bloque)
            if 0 <= item.x + c.anchotuberias <= c.ancho_pantalla + c.anchotuberias:
                if item.tipo == 5:
                    if item.y == 144:
                        pyxel.blt(item.x, item.y, 0, 38, 132, c.alturatuberia_pequeña, c.alturatuberia_pequeña)
                    else:
                        pyxel.blt(item.x, item.y, 0, 79, 178, c.anchotuberias, c.alturatuberia_grande)

        #dibuja los enemigos dependiendo de su tipo
        for item in self.__enemigos:
            if item.vivo == True:
                if item.tipo == 1: #Dibuja a los Goomba
                    if 0 <= item.x + c.anchura_goomba <= c.ancho_pantalla + c.anchura_goomba:
                        pyxel.blt(item.x, item.y, 1, 1, 0, c.anchura_goomba, c.altura_goomba, 12)
                else:               #Dibuja a los KoopaTroopa
                    if 0 <= item.x + c.anchura_koopa <= c.ancho_pantalla + c.anchura_koopa:
                        pyxel.blt(item.x, item.y, 1, 23, 0, c.anchura_koopa, c.altura_koopa, 12)

        # dibuja a Mario a medida que se va moviendo
        pyxel.blt(self.__mario.x, self.__mario.y, 0, 2, 97, 13, 16, 12)

        # dibuja "MARIO"
        pyxel.blt(10, 1, 0, 15, 7, 40, 9)

        # Dibuja el marcador
        pyxel.blt(10, 12, 0, 16, 16, 48, 7)

        # Dibuja contador monedas
        pyxel.blt(64, 12, 0, 80, 16, 31, 9)

        #Dibuja el temporizador
        pyxel.text(220, 7, str(self.__cuenta_atras), 7)

Juego()
