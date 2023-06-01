"""Solorzano Galvez Gilberto Jesus"""
import pygame
import sys

#cptura los datos de las cordenadas para dibujar a la linea del punto a al punto b
def posicion_linea():
    global x1
    global y1
    global x2
    global y2
    global size
    coordenadas_tamanio= input(" ")
    valores= coordenadas_tamanio.split()            
    # Verificar que se hayan ingresado los 3 valores
    if len(valores) == 4:
        x1 = int(valores[0])
        y1 = int(valores[1])
        x2 = int(valores[0])
        y2 = int(valores[1])
        #size = int(valores[2])*42
    else:
        print("alert: error a falta de datos")
#dibujar la linea desde pinto a hasta punto b
def linea_d(surface, color, x1_ab, y1_ab, x2_ab, y2_ab):
    dx = abs(x2_ab - x1_ab)
    dy = abs(y2_ab - y1_ab)
    sx = -1 if x1_ab > x2_ab else 1
    sy = -1 if y1_ab > y2_ab else 1
    error = dx - dy

    while x1_ab != x2_ab or y1_ab != y2_ab:
        surface.set_at((x1_ab, y1_ab), color)
        e2 = 2 * error
        if e2 > -dy:
            error -= dy
            x1_ab += sx
        if e2 < dx:
            error += dx
            y1_ab += sy
    pygame.display.flip()

#funcion para capturar punto a y punto b
def llamar_ab():
    ab = cmd.split(" ")
    global x1_ab
    global y1_ab
    global x2_ab
    global y2_ab
    if len(ab) == 5 :
        print("Si entro")
        x1_ab = int(ab[1])
        y1_ab= int(ab[2])
        x2_ab = int(ab[3])
        y2_ab= int(ab[4])
        linea_d(surface, color, x1_ab, y1_ab, x2_ab, y2_ab)
        

    else: print("datos incompletos")

#pide cordenadas y medida del cuadrado
def posicion_c():
    cuadrito = cmd.split(" ")
    global x_c 
    global y_c
    global size_c
    if len(cuadrito) == 5:
        print("Si entro")
        x_c = int(cuadrito[2])
        y_c = int(cuadrito[3])
        size_c = int(cuadrito[4])*42
        cuadro(surface,x_c,y_c,size_c,color)
    else: print("datos incompletos")

#dibuja el cuadrado
def cuadro(surface, x, y, size, color):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size-1 or j == 0 or j == size-1:
                surface.set_at((x + i, y + j), color)
    pygame.display.flip()

def rectangulo(surface,x_r,y_r,base_r,altura_r,color):
    for i in range(base_r):
        for j in range(altura_r):
            if i == 0 or i == base_r-1 or j == 0 or j == altura_r-1:
                surface.set_at((x_r + i, y_r + j), color)
    pygame.display.flip()

#pedir datos de rectangulo 
def datos_rect():
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

def linea_h(x,y,size,color):
    for i in range(0, size):
        surface.set_at(( x + i, y), color)
    ## Mostrar la superficie en la pantalla
    pygame.display.flip()

def linea_v(x,y,size,color):
    for i in range(0,size):
        surface.set_at((x, y + i), color)
    pygame.display.flip()
def posicion():
    global x 
    global y
    global size
    coordenadas_tamanio= input(" ")
    valores= coordenadas_tamanio.split()            
    # Verificar que se hayan ingresado los 3 valores
    if len(valores) == 3:
        x = int(valores[0])
        y = int(valores[1])
        size = int(valores[2])*42
    else:
        print("alert: error a falta de datos")


# Inicializar Pygame
pygame.init()

#imprime la pantalla de 800x600
width = 800
height = 600
surface = pygame.display.set_mode((width, height))
# Establecer el color de fondo de la superficie
background_color = (255, 255, 255)
surface.fill(background_color)

#listas para guardar posiciones de las figuras, asi a la hora de cambiar el color manda a llamar la info y se re imprimen
cache_lineav = []
cache_lineah = []
cache_cuadrado = []
cache_ab = []
cache_rect = []

# Color de inicio 
color = (255, 0, 0)

while True:
    cmd = input("cmd> ")
#Figuras

    if "draw cuadro" in cmd:
        posicion_c()
        cache_cuadrado.append((surface,x_c,y_c,size_c,color))
        cuadro(surface, x_c, y_c, size_c, color)

    elif "draw rect" in cmd:
        datos_rect()
        cache_rect.append((surface,x_r,y_r,base_r,altura_r,color))

    elif "lineab" in cmd:
        print("Linea a b")
        llamar_ab()
        cache_ab.append((surface, color, x1_ab, y1_ab, x2_ab, y2_ab))

    elif cmd == "linea -h":
        print("Linea horizontal")
        posicion()
        cache_lineah.append((x,y,size,color))
        linea_h(x,y,size,color)

    elif cmd == "linea -v":
        posicion()
        cache_lineav.append((x,y,size,color))
        linea_v(x,y,size,color)


#COLOR LINEA
    elif cmd == "color -ls":
        print("azul: color set azul \n rojo:  color set rojo\n verde: color set verde\n morado color set morado")
    elif cmd == "color set azul":
        color = (0, 0, 255)
        print("El color cambio a azul")
    elif color == "color set rojo":
        color=(255,0,0)
        print("El color cambio a rojo")
    elif cmd == "color set verde":
        color=(0, 128, 0)
        print("El color cambio a verde")
    elif cmd == "color set morado":
        print("El color cambio a morado")
        color=(128, 0, 128)


#COLOR FONDO
    elif cmd == "fondo ls":
        print("negro: fondo set negro")
        print("blanco: fondo set blanco")
    elif cmd == "fondo set negro":
        background_color = (0, 0, 0)
        surface.fill(background_color)
        for dato in cache_lineah:
            linea_h(dato[0], dato[1], dato[2], dato[3])
        for dato in cache_lineav:
            linea_v(dato[0], dato[1], dato[2], dato[3])
        for dato in cache_cuadrado:
            cuadro(dato[0], dato[1], dato[2], dato[3],  dato[4])
        for dato in cache_rect:
            rectangulo(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5])
        for dato in cache_ab:
            linea_d(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5])
        print("el color de fondo cambio a negro")

    elif cmd == "fondo set blanco":
        background_color = (255, 255, 255)
        surface.fill(background_color)
        for dato in cache_lineah:
            linea_h(dato[0], dato[1], dato[2], dato[3])
        for dato in cache_lineav:
            linea_v(dato[0], dato[1], dato[2], dato[3])
        for dato in cache_cuadrado:
            cuadro(dato[0], dato[1], dato[2], dato[3], dato[4])
        for dato in cache_rect:
            rectangulo(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5])
        for dato in cache_ab:
            linea_d(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5])

        print("el color de fondo cambio a blanco")

#tamaño pixel

#SALIR
    elif cmd == "exit":
        pygame.quit()
        sys.exit()
    else: 
        ("comando invalido")
