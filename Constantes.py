#En este fichero guardaremos las constantes que se usen a lo largo del videojuego
#Así, si en algún momento hay que cambiarlas solo hace falta cambiarlas en este archivo

#Pantalla
ancho_pantalla = 256
alto_pantalla = 200
mitad_pantalla = 128
longitud_juego = 1568
velocidad = 2
n_frames = 30
duracion_juego = 300

#Suelo
altura_suelo = 23
anchura_suelo = 16
n_bloques = longitud_juego // anchura_suelo

#Mario
anchura_Mario = 13
altura_Mario = 16
posicion_inicialX = 23
posicion_inicialY = alto_pantalla - altura_suelo - altura_Mario
velocidad_Mario_x = 2
velocidad_salto_x = 2
variacion_y = 0
velocidad_Mario_y= 11
vidas = 3

#Bloques
tamaño_bloque = 16 #Son cuadrados
altura_1 = 121
altura_2 = 70
alturatuberia_pequeña = 33
alturatuberia_grande = 50
anchotuberias = 32

#enemigos
velocidad_enemigos_x = 1
velocidad_enemigos_y = 1
altura_goomba = 16
anchura_goomba = 16
anchura_enemigos = 16
altura_koopa = 26
anchura_koopa = 17

