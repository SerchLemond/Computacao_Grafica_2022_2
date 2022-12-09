import sdl2
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    ( 0,-2, 0), #0
    (-1,-2, 1), #1
    ( 0,-2, 2), #2
    ( 2,-2, 2), #3
    ( 3,-2, 1), #4
    ( 2,-2, 0), #5
    ( 1,-2, 1), #6(C)
    ( 0, 2, 0), #7
    (-1, 2, 1), #8
    ( 0, 2, 2), #9
    ( 2, 2, 2), #10
    ( 3, 2, 1), #11
    ( 2, 2, 0), #12
    ( 1, 2, 1), #13(C)
    )

linhas = (
    (0,1),
    (1,2),
    (2,3),
    (3,4),
    (4,5),
    (5,0),
    (7,8),
    (8,9),
    (9,10),
    (10,11),
    (0,7),
    (1,8),
    (2,9),
    (3,10),
    (4,11),
    (5,12),
    )

faces = (
    (0,1,6,5),
    (2,3,6,1),
    (4,5,6,3),
    (7,8,13,12),
    (9,10,13,8),
    (11,12,13,10),
    (0,1,8,7),
    (1,2,9,8),
    (2,3,10,9),
    (3,4,11,10),
    (4,5,12,11),
    (5,0,7,12),
    )

cores = ((1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,0),(1,1,0),(0,1,1),(0,0,1),(1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1))

def Prisma():
    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        for vertex in face:
           glColor3fv(cores[vertex])
           glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

a = 0

def desenhaPrismas():
    #Prisma1
    glPushMatrix()
    glTranslatef(-3,0,0)
    glRotatef(a,0,0,1)
    Prisma()
    glPopMatrix()
    #Prisma2
    glPushMatrix()
    glTranslatef(3,0,0)
    glRotatef(a,1,0,0)
    Prisma()
    glPopMatrix()
    #Prisma3
    glPushMatrix()
    glTranslatef(0,5,0)
    glRotatef(a,0,1,0)
    Prisma()
    glPopMatrix()


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(0,-2,0)
    desenhaPrismas()
    glPopMatrix()
    a += 0.1

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 2)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK,sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, 24)
sdl2.SDL_GL_SetSwapInterval(1)
window = sdl2.SDL_CreateWindow(b"Prismas", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH, WINDOW_HEIGHT, sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN)
if not window:
    sys.stderr.write("Error: Could not create window\n")
    exit(1)
glcontext = sdl2.SDL_GL_CreateContext(window)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.1, 0.0, 0.1, 1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-20)

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