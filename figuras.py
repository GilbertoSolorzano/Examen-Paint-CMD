"""figuras"""
import pygame
import sys
import math
#dibujar la linea desde pinto a hasta punto b
def linea_ab(surface, color, x1_ab, y1_ab, x2_ab, y2_ab):
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
#dibuja el cuadrado
def cuadro(surface, x, y, size, color):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size-1 or j == 0 or j == size-1:
                surface.set_at((x + i, y + j), color)
    pygame.display.flip()
#dibuja un rectangulo
def rectangulo(surface,x_r,y_r,base_r,altura_r,color):
    for i in range(base_r):
        for j in range(altura_r):
            if i == 0 or i == base_r-1 or j == 0 or j == altura_r-1:
                surface.set_at((x_r + i, y_r + j), color)
    pygame.display.flip()
#dibuja un triaangulo isoseles
def triangulo_isoseles(surface,x_i,y_i,base_i,altura_i,color):
    x1_ab = x_i
    x2_ab = x_i + base_i
    x3_ab = x_i + base_i // 2
    y1_ab = y_i
    y2_ab = y_i
    y3_ab = y_i - altura_i
    linea_d(surface,color,x1_ab,y1_ab,x2_ab,y2_ab)
    linea_d(surface,color,x2_ab,y2_ab,x3_ab,y3_ab)
    linea_d(surface,color,x3_ab,y3_ab,x1_ab,y1_ab)
#imprime un triangulo escaleno
def triangulo_escaleno(surface,x_t,y_t,base_t,altura_t,color):
    x1_ab = x_t
    x2_ab = x_t
    y1_ab = y_t
    y2_ab = y_t
    for i in range(base_t):
        surface.set_at((x1_ab, y1_ab), color)
        x1_ab+=1
    for i in range(altura_t):
        surface.set_at((x2_ab, y2_ab), color)
        y2_ab-=1
    linea_d(surface, color, x1_ab, y1_ab, x2_ab, y2_ab)
#imprime un triangulo equilatero
def triangulo_equilatero(surface,x_e,y_e,base_e,color):
    angulo = math.radians(60)
    x1_ab = x_e
    y1_ab = y_e
    x2_ab = x_e + base_e
    y2_ab = y_e
    x3_ab = x_e + base_e // 2
    y3_ab = y_e - int(math.sin(angulo)*base_e)
    linea_d(surface,color,x1_ab,y1_ab,x2_ab,y2_ab)
    linea_d(surface,color,x2_ab,y2_ab,x3_ab,y3_ab)
    linea_d(surface,color,x3_ab,y3_ab,x1_ab,y1_ab)
#dibuja un circulo
def circulo(surface,x_cir,y_cir,radio,color):
    puntos = 1000
    angle_step = 2 * math.pi / puntos
    for i in range (puntos): 
        angulo = i * angle_step
        x = x_cir + int(radio*math.cos(angulo))
        y = y_cir + int(radio*math.sin(angulo))
        surface.set_at((x,y), color)
        pygame.display.flip()
