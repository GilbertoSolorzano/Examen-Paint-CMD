"""Solorzano Galvez Gilberto Jesus"""
from figuras import linea_ab, cuadro, rectangulo
from figuras import triangulo_isoseles, triangulo_escaleno
from figuras import triangulo_equilatero, circulo
import pygame
import sys
import math
# pylint: disable=C0103
# pylint: disable=C0411
# pylint: disable=W0105
def listas():
    for dato in cache_cuadrado:
        cuadro(*dato)
    for dato in cache_rect:
        rectangulo(*dato)
    for dato in cache_ab:
        linea_ab(*dato)
    for dato in cache_tr_esq:
        triangulo_escaleno(*dato)
    for dato in cache_tr_equilatero:
        triangulo_equilatero(*dato)
    for dato in cache_tr_isoleses:
        triangulo_isoseles(*dato)
    for dato in cache_circulo:
        circulo(*dato)
# Esta función guarda las figuras que 
#van siendo creadas ensu respectiva lista
#para poder eliminar de uno en uno los dibujos
def undo(surface,
    cache_ab,
    cache_rect,
    cache_tr_esq,
    cache_cuadrado,
    cache_tr_equilatero,
    cache_tr_isoleses,
    cache_circulo):
    if len(cache_ab) > 0:
        cache_ab.pop()
    elif len(cache_rect) > 0:
        cache_rect.pop()
    elif len(cache_tr_esq) > 0:
        cache_tr_esq.pop()
    elif len(cache_cuadrado) > 0:
        cache_cuadrado.pop()
    elif len(cache_tr_equilatero) > 0:
        cache_tr_equilatero.pop()
    elif len(cache_tr_isoleses) > 0:
        cache_tr_isoleses.pop()
    elif len(cache_circulo) > 0:
        cache_circulo.pop()
    else:
        print("No hay trazos para borrar")
    surface.fill(background_color)
    listas()
    pygame.display.flip()
def llamar_ab():
    """captura los datos de las cordenadas para dibujar a la linea del punto a al punto b"""
    ab = cmd.split(" ")
    global x1_ab
    global y1_ab
    global x2_ab
    global y2_ab
    if len(ab) == 5 :
        x1_ab = int(ab[1])
        y1_ab= int(ab[2])
        x2_ab = int(ab[3])
        y2_ab= int(ab[4])
        linea_ab(surface, color, x1_ab, y1_ab, x2_ab, y2_ab)
    else: print("datos incompletos")
def posicion_c():
    """pide cordenadas y medida del cuadrado """
    cuadrito = cmd.split(" ")
    global x_c
    global y_c
    global size_c
    if len(cuadrito) == 5:
        x_c = int(cuadrito[2])
        y_c = int(cuadrito[3])
        size_c = int(cuadrito[4])*42
        cuadro(surface,x_c,y_c,size_c,color)
    else: print("datos incompletos")
def datos_rect():
    """pedir datos de rectangulo"""
    rect = cmd.split(" ")
    # eje x de rectangulo
    global x_r
    global y_r
    global base_r
    global altura_r
    if len(rect) == 6:
        x_r = int(rect[2])
        y_r = int(rect[3])
        base_r = int(rect[4])*42
        altura_r = int(rect[5])*42
        rectangulo(surface,x_r,y_r,base_r,altura_r,color)
    else: ("datos incompletos")
#pide datos de triangulo equilatero
def datos_equi():
    equi = cmd.split(" ")
    global x_e
    global y_e
    global base_e
    if len(equi) == 5:
        x_e = int(equi[2])
        y_e = int(equi[3])
        base_e = int(equi[4])*42
        triangulo_equilatero(surface,x_e,y_e,base_e,color)
    else: ("datos incompletos")
def datos_tri_escaleno():
    """pide datos de triangulo escaleno"""
    rect = cmd.split(" ")
    global x_t
    global y_t
    global base_t
    global altura_t
    if len(rect) == 6:
        x_t = int(rect[2])
        y_t = int(rect[3])
        base_t = int(rect[4])*42
        altura_t = int(rect[5])*42
        triangulo_escaleno(surface,x_t,y_t,base_t,altura_t,color)
    else: ("datos incompletos")
#pide los datos de un tringulo isoseles
def datos_tri_isoseles():
    iso = cmd.split(" ")
    global x_i
    global y_i
    global base_i
    global altura_i
    if len(iso) == 6:
        x_i = int(iso[2])
        y_i = int(iso[3])
        base_i = int(iso[4])*42
        altura_i = int(iso[5])*42
        triangulo_isoseles(surface,x_i,y_i,base_i,altura_i,color)
    else: ("datos incompletos")
#pide los datos deun circulo
def datos_circulo():
    circ = cmd.split(" ")
    global x_cir
    global y_cir
    global radio
    if len(circ) == 5:
        x_cir = int(circ[2])
        y_cir = int(circ[3])
        radio = int(circ[4])*42
        circulo(surface,x_cir,y_cir,radio,color)
    else: ("datos incompletos")
pygame.init()
#imprime la pantalla de 800x600
width = 800
height = 600
surface = pygame.display.set_mode((width, height))
# Establecer el color de fondo de la superficie
background_color = (255, 255, 255)
surface.fill(background_color)
#listas para guardar posiciones
#de las figuras, asi a la hora de
#cambiar el color manda a llamar
#la info y se re imprimen
cache_cuadrado = []
cache_ab = []
cache_rect = []
cache_tr_esq = []
cache_tr_equilatero = []
cache_tr_isoleses = []
cache_circulo = []
# Color de inicio
color = (255, 0, 0)
while True:
    cmd = input("cmd> ")
    #Figuras
    if "draw cuadro" in cmd:
        posicion_c()
        cache_cuadrado.append((surface,x_c,y_c,size_c,color))
    elif "draw rect" in cmd:
        datos_rect()
        cache_rect.append((surface,x_r,y_r,base_r,altura_r,color))
    elif "draw tr-es" in cmd:
        datos_tri_escaleno()
        cache_tr_esq.append((surface,x_t,y_t,base_t,altura_t,color))
    elif "draw tr-eq" in cmd:
        datos_equi()
        cache_tr_equilatero.append((surface,x_e,y_e,base_e,color))
    elif "draw tr-is" in cmd:
        datos_tri_isoseles()
        cache_tr_isoleses.append((surface,x_i,y_i,base_i,altura_i,color))
    elif "draw circulo" in cmd:
        datos_circulo()
        cache_circulo.append((surface,x_cir,y_cir,radio,color))
        circulo(surface,x_cir,y_cir,radio,color)
    elif "lineab" in cmd:
        llamar_ab()
        cache_ab.append((surface, color, x1_ab, y1_ab, x2_ab, y2_ab))
    #borrar
    elif cmd == "undo":
        undo(surface, cache_ab, cache_rect,
            cache_tr_esq, cache_cuadrado,
            cache_tr_equilatero,cache_tr_isoleses,
            cache_circulo)
#COLOR LINEA
    elif cmd == "color -ls":
        print("azul: color set azul \n rojo:  color set rojo\n")
        print("verde: color set verde\n morado: color set morado\n")
        print("negro: color set negro\n blanco: color set blanco")
    elif cmd == "color set azul":
        color = (0, 0, 255)
        print("El color de la linea cambio a azul")
    elif cmd == "color set blanco":
        color = (0, 0, 255)
        print("El color de la linea cambio a blanco")
    elif cmd == "color set negro":
        color = (0, 0, 0)
        print("El color de la linea cambio a negro")
    elif color == "color set rojo":
        color=(255,0,0)
        print("El color de la linea cambio a rojo")
    elif cmd == "color set verde":
        color=(0, 128, 0)
        print("El color de la linea cambio a verde")
    elif cmd == "color set morado":
        color=(128, 0, 128)
        print("El color de la linea cambio a morado")
#COLOR FONDO
    elif cmd == "fondo ls":
        print("negro: fondo set negro")
        print("blanco: fondo set blanco")
        print("azul: fondo set azul")
        print("rojo:  fondo set rojo")
        print("verde: fondo set verde")
        print("morado: fondo set morado")
    elif cmd == "fondo set negro":
        background_color = (0, 0, 0)
        surface.fill(background_color)
        listas()
        print("el color de fondo cambio a negro")
    elif cmd == "fondo set azul":
        background_color = (0, 0, 255)
        surface.fill(background_color)
        listas()
        print("el color de fondo cambio a azul")
    elif cmd == "fondo set rojo":
        background_color = (255,0,0)
        surface.fill(background_color)
        listas()
        print("el color de fondo cambio a rojo")
    elif cmd == "fondo set verde":
        background_color = (0, 128, 0)
        surface.fill(background_color)
        listas()
        print("el color de fondo cambio a verde")
    elif cmd == "fondo set morado":
        background_color = (128, 0, 128)
        surface.fill(background_color)
        listas()
        print("el color de fondo cambio a morado")
    elif cmd == "fondo set blanco":
        background_color = (255, 255, 255)
        surface.fill(background_color)
        listas()
        print("el color de fondo cambio a blanco")
    elif cmd == "help":
        global contenido
        with open('about.txt','r',encoding="utf-8") as f:
            contenido = f.read()
        print(contenido)
    #SALIR
    elif cmd == "exit":
        pygame.quit()
        sys.exit()
    else:
        ("comando invalido")
