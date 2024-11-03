import math

import pygame
from pygame.locals import *
import numpy as np

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpMat import OpMat
from Robot import Robot
from OpenGL.GLUT import *

pygame.init()

opera = OpMat()
t1 = Robot(opera)
t2 = Robot(opera)
screen_width = 900
screen_height = 600

# Variables para dibujar los ejes del sistema
X_MIN = -500
X_MAX = 500
Y_MIN = -500
Y_MAX = 500

def Axis():
    glShadeModel(GL_FLAT)
    glLineWidth(3.0)
    # X axis in red
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(X_MIN, 0.0)
    glVertex2f(X_MAX, 0.0)
    glEnd()
    # Y axis in green
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(0.0, Y_MIN)
    glVertex2f(0.0, Y_MAX)
    glEnd()
    glLineWidth(1.0)



#variables de control
deg = 0
deltaDeg = 0
degrot = 0
def display():
    global deg
    global deg1
    global degrot
    global delta_degrot
    glClear(GL_COLOR_BUFFER_BIT)
    Axis()
    opera.push()
    opera.rotation(deg)
    opera.scale(10,10)
    t1.setColor(1,1,0)
    t1.render()
    opera.pop()
    deg = (deg + deltaDeg ) % 360
    degrot = (degrot + deltaDeg) % 360


def init():
    screen = pygame.display.set_mode(
        (screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL: ejes 2D")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-450, 450, -300, 300)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClearColor(0, 0, 0, 0)
    # OPCIONES: GL_LINE, GL_POINT, GL_FILL
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glShadeModel(GL_FLAT)


def draw_point(x, y):
    glColor3f(1.0, 0.0, 0.0)  # Set the color to red
    glPointSize(5.0)  # Set the point size to 5.0
    glBegin(GL_POINTS)  # Start drawing points
    glVertex2f(x, y)  # Specify the position of the point
    glEnd()  # Done specifying points


# código principal ---------------------------------
init()




#Matrices para operaciones geometricas

A = np.identity(3) #matriz de modelado
T = np.identity(3) #matriz para la traslacion
R = np.identity(3) #matriz para rotacion
E = np.identity(3) #matriz de escalado


def Axis():
    glShadeModel(GL_FLAT)
    glLineWidth(3.0)
    # X axis in red
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(X_MIN, 0.0)
    glVertex2f(X_MAX, 0.0)
    glEnd()
    # Y axis in green
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(0.0, Y_MIN)
    glVertex2f(0.0, Y_MAX)
    glEnd()
    glLineWidth(1.0)




done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                t1.move_forward()  # Mueve el carrito hacia adelante
            elif event.key == pygame.K_DOWN:
                t1.move_backward()  # Mueve el carrito hacia atrás
            elif event.key == pygame.K_LEFT:
                t1.girar(90)  # Gira 90 grados a la izquierda
            elif event.key == pygame.K_RIGHT:
                t1.girar(-90)  # Gira 90 grados a la derecha

    glClear(GL_COLOR_BUFFER_BIT)
    Axis()
    glPointParameterf(GL_POINT_SIZE_MAX, 100.0)
    display()
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
