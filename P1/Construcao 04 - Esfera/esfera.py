import math
import sys

import sdl2
from OpenGL.GL import *
from OpenGL.GLU import *


def Esfera(n, r):
    glBegin(GL_POINTS)
    for i in range(n):
        teta = ((math.pi * i)/n) - (math.pi/2)
        for j in range(n):
            phi = (2 * math.pi * j)/n
            x = r * math.cos(teta) * math.cos(phi)
            y = r * math.sin(teta)
            z = r * math.cos(teta) * math.sin(phi)
            glVertex3f(x, y, z)
    glEnd()

ar = 0

def desenha():
    global ar
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(ar, 1, 1, 1)
    Esfera(20, 3)
    glPopMatrix()
    ar += 0.1


WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700

sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 2)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK, sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, 24)
sdl2.SDL_GL_SetSwapInterval(1)
window = sdl2.SDL_CreateWindow(b"Esfera", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH,
                               WINDOW_HEIGHT, sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN)
if not window:
    sys.stderr.write("Error: Could not create window\n")
    exit(1)
glcontext = sdl2.SDL_GL_CreateContext(window)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.1, 0.0, 0.1, 1.)
gluPerspective(45, 700.0 / 700.0, 0.1, 100.0)
glTranslatef(0.0, 0.0, -10)

running = True
event = sdl2.SDL_Event()
while running:
    while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_QUIT:
            running = False
        if event.type == sdl2.events.SDL_KEYDOWN:
            print("SDL_KEYDOWN")
            if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                running = False
    desenha()
    sdl2.SDL_GL_SwapWindow(window)