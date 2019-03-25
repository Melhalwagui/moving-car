from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def draw_XYZ():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex(0, 0, 0)
    glVertex(10, 0, 0)

    glColor3f(0, 1, 0)
    glVertex(0, 0, 0)
    glVertex(0, 10, 0)

    glColor3f(0, 0, 1)
    glVertex(0, 0, 0)
    glVertex(0, 0, 10)
    glEnd()


def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 30)
    gluLookAt(8, 9, 10,
              0, 0, 0,
              0, 1, 0)

    glClearColor(1, 1, 1, 1)


angle = 0
x = 0
forward = True


def draw():
    global angle
    global x
    global forward

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_QUADS)
    glColor3f(0.2, 1, 0.5)
    glVertex(-20, 0, 2)
    glVertex(10, 0, 2)
    glVertex(10, 0, 10)
    glVertex(-20, 0, 10)
    glEnd()
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.6, 0.5)
    glVertex(-25, 2, 0)
    glVertex(10, 2, 0)
    glVertex(10, -5, 0)
    glVertex(-25, -5, 0)
    glEnd()
    glBegin(GL_QUADS)
    glColor3f(0.2, 1, 0.5)
    glVertex(-30, -5, 0)
    glVertex(10, -5, 0)
    glVertex(10, -25, 0)
    glVertex(-30, -25, 0)
    glEnd()
    glBegin(GL_QUADS)
    glColor3f(1,1,1)
    for i in range(-20,20,8):
        glVertex(i, 0, 0.5)
        glVertex(i, 0, 1)
        glVertex(i + 4, 0, 1)
        glVertex(i+4, 0, 0.5)
    glEnd()








    draw_XYZ()

    glColor3f(1, 0, 0)
    glTranslate(x, 0, 0)
    glScale(1, 0.25, 0.5)
    glutWireCube(5)

    glLoadIdentity()
    glTranslate(x, 5*0.25, 0)
    glScale(0.5, 0.25, 0.5)
    glutWireCube(5)

    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x+0.5*5, -0.5 * 0.25*5, 0.5 * 0.5*5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()
    glTranslate(x+0.5*5, -0.5 * 0.25*5, - 0.5 * 0.5*5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()
    glTranslate(x-0.5*5, -0.5 * 0.25*5, -0.5 * 0.5*5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()
    glTranslate(x-0.5*5, -0.5 * 0.25*5, 0.5 * 0.5*5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 10, 10)
    glutSwapBuffers()

    if forward:
        angle -= 0.1
        x += 0.002
        if x > 5:
            forward = False
    else:
        angle += 0.1
        x -= 0.002
        if x < -5:
            forward = True


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car")
myInit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
