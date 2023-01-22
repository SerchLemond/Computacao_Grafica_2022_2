from GLAPP import GLAPP
from OpenGL import GL
from array import array
import ctypes
import glm
import math

class SateliteF(GLAPP):

    def setup(self):
        # Window setup
        self.title("LowPoly Satelite")
        self.size(700,600)

        # OpenGL Initialization
        GL.glClearColor(0.0, 0.0, 0.0, 0.0)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_MULTISAMPLE)

        # Pipeline (shaders)
        self.pipeline1 = self.loadPipeline("SimpleTexture")
        self.pipeline2 = self.loadPipeline("WhiteDotsPipeline")
        self.a = 0
        self.b = 0
        self.c = 0

        # Texture
        GL.glActiveTexture(GL.GL_TEXTURE0)
        self.loadTexture("./textures/t1.png")
        GL.glUseProgram(self.pipeline1)
        GL.glUniform1i(GL.glGetUniformLocation(self.pipeline1, "textureSlot"),0)

        self.squareArrayBufferId = None
        self.sphereArrayBufferId = None

    def drawSatelite(self):
        #PONTOS{
        
        #A1 = -1.0,  3.0,  0.0
        #A2 = -1.0,  3.0,  4.0
        #A3 = -1.0,  3.0,  5.0
        #A4 = -1.0,  3.0,  8.0

        #B1 =  1.0,  3.0,  0.0
        #B2 =  1.0,  3.0,  4.0
        #B3 =  1.0,  3.0,  5.0
        #B4 =  1.0,  3.0,  8.0

        #C1 =  3.0,  1.0,  0.0
        #C2 =  3.0,  1.0,  4.0
        #C3 =  3.0,  1.0,  5.0
        #C4 =  3.0,  1.0,  8.0

        #D1 =  3.0, -1.0,  0.0
        #D2 =  3.0, -1.0,  4.0
        #D3 =  3.0, -1.0,  5.0
        #D4 =  3.0, -1.0,  8.0

        #E1 =  1.0, -3.0,  0.0
        #E2 =  1.0, -3.0,  4.0
        #E3 =  1.0, -3.0,  5.0
        #E4 =  1.0, -3.0,  8.0

        #F1 = -1.0, -3.0,  0.0
        #F2 = -1.0, -3.0,  4.0
        #F3 = -1.0, -3.0,  5.0
        #F4 = -1.0, -3.0,  8.0

        #G1 = -3.0, -1.0,  0.0
        #G2 = -3.0, -1.0,  4.0
        #G3 = -3.0, -1.0,  5.0
        #G4 = -3.0, -1.0,  8.0

        #H1 = -3.0,  1.0,  0.0
        #H2 = -3.0,  1.0,  4.0
        #H3 = -3.0,  1.0,  5.0
        #H4 = -3.0,  1.0,  8.0

        ########

        #V2 =  0.0,  2.0,  4.0
        #V3 =  0.0,  2.0,  5.0
        #V4 =  0.0,  2.0,  8.0
        #V5 =  0.0,  2.0,  9.0

        #W2 =  2.0,  0.0,  4.0
        #W3 =  2.0,  0.0,  5.0
        #W4 =  2.0,  0.0,  8.0
        #W5 =  2.0,  0.0,  9.0

        #X2 =  0.0, -2.0,  4.0
        #X3 =  0.0, -2.0,  5.0
        #X4 =  0.0, -2.0,  8.0
        #X5 =  0.0, -2.0,  9.0

        #Y2 = -2.0,  0.0,  4.0
        #Y3 = -2.0,  0.0,  5.0
        #Y4 = -2.0,  0.0,  8.0
        #Y5 = -2.0,  0.0,  9.0

        ########

        #Z1 =  0.0,  0.0,  0.0
        #Z2 =  0.0,  0.0,  4.0
        #Z3 =  0.0,  0.0,  5.0
        #Z4 =  0.0,  0.0,  8.0

        ########

        #J1 = -6.0,  2.0,  1.0
        #J2 = -3.0,  2.0,  1.0
        #J3 =  3.0,  2.0,  1.0
        #J4 =  6.0,  2.0,  1.0

        #K1 = -6.0, -2.0,  3.0
        #K2 = -3.0, -2.0,  3.0
        #K3 =  3.0, -2.0,  3.0
        #K4 =  6.0, -2.0,  3.0
        
        #M1 = -6.0,  2.0,  6.0
        #M2 = -3.0,  2.0,  6.0
        #M3 =  3.0,  2.0,  6.0
        #M4 =  6.0,  2.0,  6.0
        
        #N1 = -6.0, -2.0,  7.0
        #N2 = -3.0, -2.0,  7.0
        #N3 =  3.0, -2.0,  7.0
        #N4 =  6.0, -2.0,  7.0
#       }

        if self.squareArrayBufferId == None:
            position = array('f',[
                 0.0,  0.0,  0.0, # Z1
                -1.0,  3.0,  0.0, # A1
                 1.0,  3.0,  0.0, # B1
                 0.0,  0.0,  0.0, # Z1
                 1.0,  3.0,  0.0, # B1
                 3.0,  1.0,  0.0, # C1
                 0.0,  0.0,  0.0, # Z1
                 3.0,  1.0,  0.0, # C1
                 3.0, -1.0,  0.0, # D1
                 0.0,  0.0,  0.0, # Z1
                 3.0, -1.0,  0.0, # D1
                 1.0, -3.0,  0.0, # E1
                 0.0,  0.0,  0.0, # Z1
                 1.0, -3.0,  0.0, # E1
                -1.0, -3.0,  0.0, # F1
                 0.0,  0.0,  0.0, # Z1
                -1.0, -3.0,  0.0, # F1
                -3.0, -1.0,  0.0, # G1
                 0.0,  0.0,  0.0, # Z1
                -3.0, -1.0,  0.0, # G1
                -3.0,  1.0,  0.0, # H1
                 0.0,  0.0,  0.0, # Z1
                -3.0,  1.0,  0.0, # H1
                -1.0,  3.0,  0.0, # A1

                 0.0,  0.0,  4.0, # Z2
                -1.0,  3.0,  4.0, # A2
                 1.0,  3.0,  4.0, # B2
                 0.0,  0.0,  4.0, # Z2
                 1.0,  3.0,  4.0, # B2
                 3.0,  1.0,  4.0, # C2
                 0.0,  0.0,  4.0, # Z2
                 3.0,  1.0,  4.0, # C2
                 3.0, -1.0,  4.0, # D2
                 0.0,  0.0,  4.0, # Z2
                 3.0, -1.0,  4.0, # D2
                 1.0, -3.0,  4.0, # E2
                 0.0,  0.0,  4.0, # Z2
                 1.0, -3.0,  4.0, # E2
                -1.0, -3.0,  4.0, # F2
                 0.0,  0.0,  4.0, # Z2
                -1.0, -3.0,  4.0, # F2
                -3.0, -1.0,  4.0, # G2
                 0.0,  0.0,  4.0, # Z2
                -3.0, -1.0,  4.0, # G2
                -3.0,  1.0,  4.0, # H2
                 0.0,  0.0,  4.0, # Z2
                -3.0,  1.0,  4.0, # H2
                -1.0,  3.0,  4.0, # A2

                 0.0,  0.0,  5.0, # Z3
                -1.0,  3.0,  5.0, # A3
                 1.0,  3.0,  5.0, # B3
                 0.0,  0.0,  5.0, # Z3
                 1.0,  3.0,  5.0, # B3
                 3.0,  1.0,  5.0, # C3
                 0.0,  0.0,  5.0, # Z3
                 3.0,  1.0,  5.0, # C3
                 3.0, -1.0,  5.0, # D3
                 0.0,  0.0,  5.0, # Z3
                 3.0, -1.0,  5.0, # D3
                 1.0, -3.0,  5.0, # E3
                 0.0,  0.0,  5.0, # Z3
                 1.0, -3.0,  5.0, # E3
                -1.0, -3.0,  5.0, # F3
                 0.0,  0.0,  5.0, # Z3
                -1.0, -3.0,  5.0, # F3
                -3.0, -1.0,  5.0, # G3
                 0.0,  0.0,  5.0, # Z3
                -3.0, -1.0,  5.0, # G3
                -3.0,  1.0,  5.0, # H3
                 0.0,  0.0,  5.0, # Z3
                -3.0,  1.0,  5.0, # H3
                -1.0,  3.0,  5.0, # A3
                
                 0.0,  0.0,  9.0, # Z4
                -1.0,  3.0,  9.0, # A4
                 1.0,  3.0,  9.0, # B4
                 0.0,  0.0,  9.0, # Z4
                 1.0,  3.0,  9.0, # B4
                 3.0,  1.0,  9.0, # C4
                 0.0,  0.0,  9.0, # Z4
                 3.0,  1.0,  9.0, # C4
                 3.0, -1.0,  9.0, # D4
                 0.0,  0.0,  9.0, # Z4
                 3.0, -1.0,  9.0, # D4
                 1.0, -3.0,  9.0, # E4
                 0.0,  0.0,  9.0, # Z4
                 1.0, -3.0,  9.0, # E4
                -1.0, -3.0,  9.0, # F4
                 0.0,  0.0,  9.0, # Z4
                -1.0, -3.0,  9.0, # F4
                -3.0, -1.0,  9.0, # G4
                 0.0,  0.0,  9.0, # Z4
                -3.0, -1.0,  9.0, # G4
                -3.0,  1.0,  9.0, # H4
                 0.0,  0.0,  9.0, # Z4
                -3.0,  1.0,  9.0, # H4
                -1.0,  3.0,  9.0, # A4

                -1.0,  3.0,  0.0, # A1
                -1.0,  3.0,  4.0, # A2
                 1.0,  3.0,  4.0, # B2
                -1.0,  3.0,  0.0, # A1
                 1.0,  3.0,  0.0, # B1
                 1.0,  3.0,  4.0, # B2
                ###
                 1.0,  3.0,  0.0, # B1
                 1.0,  3.0,  4.0, # B2
                 3.0,  1.0,  4.0, # C2
                 1.0,  3.0,  0.0, # B1
                 3.0,  1.0,  0.0, # C1
                 3.0,  1.0,  4.0, # C2
                ###
                 3.0,  1.0,  0.0, # C1
                 3.0,  1.0,  4.0, # C2
                 3.0, -1.0,  4.0, # D2
                 3.0,  1.0,  0.0, # C1
                 3.0, -1.0,  0.0, # D1
                 3.0, -1.0,  4.0, # D2
                ###
                 3.0, -1.0,  0.0, # D1
                 3.0, -1.0,  4.0, # D2
                 1.0, -3.0,  4.0, # E2
                 3.0, -1.0,  0.0, # D1
                 1.0, -3.0,  0.0, # E1
                 1.0, -3.0,  4.0, # E2
                ###
                 1.0, -3.0,  0.0, # E1
                 1.0, -3.0,  4.0, # E2
                -1.0, -3.0,  4.0, # F2
                 1.0, -3.0,  0.0, # E1
                -1.0, -3.0,  0.0, # F1
                -1.0, -3.0,  4.0, # F2
                ###
                -1.0, -3.0,  0.0, # F1
                -1.0, -3.0,  4.0, # F2
                -3.0, -1.0,  4.0, # G2
                -1.0, -3.0,  0.0, # F1
                -3.0, -1.0,  0.0, # G1
                -3.0, -1.0,  4.0, # G2
                ###
                -3.0, -1.0,  0.0, # G1
                -3.0, -1.0,  4.0, # G2
                -3.0,  1.0,  4.0, # H2
                -3.0, -1.0,  0.0, # G1
                -3.0,  1.0,  0.0, # H1
                -3.0,  1.0,  4.0, # H2
                ###
                -3.0,  1.0,  0.0, # H1
                -3.0,  1.0,  4.0, # H2
                -1.0,  3.0,  4.0, # A2
                -3.0,  1.0,  0.0, # H1
                -1.0,  3.0,  0.0, # A1
                -1.0,  3.0,  4.0, # A2


                -1.0,  3.0,  5.0, # A3
                -1.0,  3.0,  9.0, # A4
                 1.0,  3.0,  9.0, # B4
                -1.0,  3.0,  5.0, # A3
                 1.0,  3.0,  5.0, # B3
                 1.0,  3.0,  9.0, # B4
                ###
                 1.0,  3.0,  5.0, # B3
                 1.0,  3.0,  9.0, # B4
                 3.0,  1.0,  9.0, # C4
                 1.0,  3.0,  5.0, # B3
                 3.0,  1.0,  5.0, # C3
                 3.0,  1.0,  9.0, # C4
                ###
                 3.0,  1.0,  5.0, # C3
                 3.0,  1.0,  9.0, # C4
                 3.0, -1.0,  9.0, # D4
                 3.0,  1.0,  5.0, # C3
                 3.0, -1.0,  5.0, # D3
                 3.0, -1.0,  9.0, # D4
                ###
                 3.0, -1.0,  5.0, # D3
                 3.0, -1.0,  9.0, # D4
                 1.0, -3.0,  9.0, # E4
                 3.0, -1.0,  5.0, # D3
                 1.0, -3.0,  5.0, # E3
                 1.0, -3.0,  9.0, # E4
                ###
                 1.0, -3.0,  5.0, # E3
                 1.0, -3.0,  9.0, # E4
                -1.0, -3.0,  9.0, # F4
                 1.0, -3.0,  5.0, # E3
                -1.0, -3.0,  5.0, # F3
                -1.0, -3.0,  9.0, # F4
                ###
                -1.0, -3.0,  5.0, # F3
                -1.0, -3.0,  9.0, # F4
                -3.0, -1.0,  9.0, # G4
                -1.0, -3.0,  5.0, # F3
                -3.0, -1.0,  5.0, # G3
                -3.0, -1.0,  9.0, # G4
                ###
                -3.0, -1.0,  5.0, # G3
                -3.0, -1.0,  9.0, # G4
                -3.0,  1.0,  9.0, # H4
                -3.0, -1.0,  5.0, # G3
                -3.0,  1.0,  5.0, # H3
                -3.0,  1.0,  9.0, # H4
                ###
                -3.0,  1.0,  5.0, # H3
                -3.0,  1.0,  9.0, # H4
                -1.0,  3.0,  9.0, # A4
                -3.0,  1.0,  5.0, # H3
                -1.0,  3.0,  5.0, # A3
                -1.0,  3.0,  9.0, # A4


                 0.0,  2.0,  4.0, # V2
                 0.0,  2.0,  5.0, # V3
                -2.0,  0.0,  5.0, # Y3
                 0.0,  2.0,  4.0, # V2
                -2.0,  0.0,  4.0, # Y2
                -2.0,  0.0,  5.0, # Y3
                ###
                -2.0,  0.0,  4.0, # Y2
                -2.0,  0.0,  5.0, # Y3
                 0.0, -2.0,  5.0, # X3
                -2.0,  0.0,  4.0, # Y2
                 0.0, -2.0,  4.0, # X2
                 0.0, -2.0,  5.0, # X3
                ###
                 0.0, -2.0,  4.0, # X2
                 0.0, -2.0,  5.0, # X3
                 2.0,  0.0,  5.0, # W3
                 0.0, -2.0,  4.0, # X2
                 2.0,  0.0,  4.0, # W2
                 2.0,  0.0,  5.0, # W3
                ###
                 2.0,  0.0,  4.0, # W2
                 2.0,  0.0,  5.0, # W3
                 0.0,  2.0,  5.0, # V3
                 2.0,  0.0,  4.0, # W2
                 0.0,  2.0,  4.0, # V2
                 0.0,  2.0,  5.0, # V3
                
                 0.0,  2.0,  9.0, # V4
                 0.0,  2.0,  10.0, # V5
                -2.0,  0.0,  10.0, # Y5
                 0.0,  2.0,  9.0, # V4
                -2.0,  0.0,  9.0, # Y4
                -2.0,  0.0,  10.0, # Y5
                ###
                -2.0,  0.0,  9.0, # Y4
                -2.0,  0.0,  10.0, # Y5
                 0.0, -2.0,  10.0, # X5
                -2.0,  0.0,  9.0, # Y4
                 0.0, -2.0,  9.0, # X4
                 0.0, -2.0,  10.0, # X5
                ###
                 0.0, -2.0,  9.0, # X4
                 0.0, -2.0,  10.0, # X5
                 2.0,  0.0,  10.0, # W5
                 0.0, -2.0,  9.0, # X4
                 2.0,  0.0,  9.0, # W4
                 2.0,  0.0,  10.0, # W5
                ###
                 2.0,  0.0,  9.0, # W4
                 2.0,  0.0,  10.0, # W5
                 0.0,  2.0,  10.0, # V5
                 2.0,  0.0,  9.0, # W4
                 0.0,  2.0,  9.0, # V4
                 0.0,  2.0,  10.0, # V5

                 0.0,  2.0,  10.0, # V5
                 2.0,  0.0,  10.0, # W5
                 0.0, -2.0,  10.0, # X5
                 0.0,  2.0,  10.0, # V5
                -2.0,  0.0,  10.0, # Y5
                 0.0, -2.0,  10.0, # X5

                -9.0, -2.0,  3.0, # K1
                -9.0,  2.0,  1.0, # J1
                -3.0,  2.0,  1.0, # J2
                -9.0, -2.0,  3.0, # K1
                -3.0, -2.0,  3.0, # K2
                -3.0,  2.0,  1.0, # J2

                 3.0, -2.0,  3.0, # K3
                 3.0,  2.0,  1.0, # J3
                 9.0,  2.0,  1.0, # J4
                 3.0, -2.0,  3.0, # K3
                 9.0, -2.0,  3.0, # K4
                 9.0,  2.0,  1.0, # J4

                -9.0, -2.0,  8.0, # N1
                -9.0,  2.0,  6.0, # M1
                -3.0,  2.0,  6.0, # M2
                -9.0, -2.0,  8.0, # N1
                -3.0, -2.0,  8.0, # N2
                -3.0,  2.0,  6.0, # M2

                 3.0, -2.0,  8.0, # N3
                 3.0,  2.0,  6.0, # M3
                 9.0,  2.0,  6.0, # M4
                 3.0, -2.0,  8.0, # N3
                 9.0, -2.0,  8.0, # N4
                 9.0,  2.0,  6.0, # M4

            ])

            textureCoord = array('f',[
                 0.25,  0.75, # Z1
                 0.0,  1.0, # A1
                 0.5,  1.0, # B1
                 0.25,  0.75, # Z1
                 0.0,  1.0, # B1
                 0.5,  1.0, # C1
                 0.25,  0.75, # Z1
                 0.0,  1.0, # C1
                 0.5,  1.0, # D1
                 0.25,  0.75, # Z1
                 0.0,  1.0, # D1
                 0.5,  1.0, # E1
                 0.25,  0.75, # Z1
                 0.0,  1.0, # E1
                 0.5,  1.0, # F1
                 0.25,  0.75, # Z1
                 0.0,  1.0, # F1
                 0.5,  1.0, # G1
                 0.25,  0.75, # Z1
                 0.0,  1.0, # G1
                 0.5,  1.0, # H1
                 0.25,  0.75, # Z1
                 0.0,  1.0, # H1
                 0.5,  1.0, # A1

                 0.25,  0.75, # Z2
                 0.0,  1.0, # A2
                 0.5,  1.0, # B2
                 0.25,  0.75, # Z2
                 0.0,  1.0, # B2
                 0.5,  1.0, # C2
                 0.25,  0.75, # Z2
                 0.0,  1.0, # C2
                 0.5,  1.0, # D2
                 0.25,  0.75, # Z2
                 0.0,  1.0, # D2
                 0.5,  1.0, # E2
                 0.25,  0.75, # Z2
                 0.0,  1.0, # E2
                 0.5,  1.0, # F2
                 0.25,  0.75, # Z2
                 0.0,  1.0, # F2
                 0.5,  1.0, # G2
                 0.25,  0.75, # Z2
                 0.0,  1.0, # G2
                 0.5,  1.0, # H2
                 0.25,  0.75, # Z2
                 0.0,  1.0, # H2
                 0.5,  1.0, # A2

                 0.25,  0.25, # Z3
                 0.0,  1.0, # A3
                 0.5,  1.0, # B3
                 0.25,  0.25, # Z3
                 0.0,  1.0, # B3
                 0.5,  1.0, # C3
                 0.25,  0.25, # Z3
                 0.0,  1.0, # C3
                 0.5,  1.0, # D3
                 0.25,  0.25, # Z3
                 0.0,  1.0, # D3
                 0.5,  1.0, # E3
                 0.25,  0.25, # Z3
                 0.0,  1.0, # E3
                 0.5,  1.0, # F3
                 0.25,  0.25, # Z3
                 0.0,  1.0, # F3
                 0.5,  1.0, # G3
                 0.25,  0.25, # Z3
                 0.0,  1.0, # G3
                 0.5,  1.0, # H3
                 0.25,  0.25, # Z3
                 0.0,  1.0, # H3
                 0.5,  1.0, # A3

                 0.25,  0.25, # Z4
                 0.0,  1.0, # A4
                 0.5,  1.0, # B4
                 0.25,  0.25, # Z4
                 0.0,  1.0, # B4
                 0.5,  1.0, # C4
                 0.25,  0.25, # Z4
                 0.0,  1.0, # C4
                 0.5,  1.0, # D4
                 0.25,  0.25, # Z4
                 0.0,  1.0, # D4
                 0.5,  1.0, # E4
                 0.25,  0.25, # Z4
                 0.0,  1.0, # E4
                 0.5,  1.0, # F4
                 0.25,  0.25, # Z4
                 0.0,  1.0, # F4
                 0.5,  1.0, # G4
                 0.25,  0.25, # Z4
                 0.0,  1.0, # G4
                 0.5,  1.0, # H4
                 0.25,  0.25, # Z4
                 0.0,  1.0, # H4
                 0.5,  1.0, # A4

                 1.0,  1.0, # A1
                 0.5,  1.0, # A2
                 0.5,  0.5, # B2
                 1.0,  1.0, # A1
                 1.0,  0.5, # B1
                 0.5,  0.5, # B2
                ###
                 0.5,  0.5, # B1
                 0.0,  0.5, # B2
                 0.0,  0.0, # C2
                 0.5,  0.5, # B1
                 0.5,  0.0, # C1
                 0.0,  0.0, # C2
                ###
                 1.0,  1.0, # C1
                 0.5,  1.0, # C2
                 0.5,  0.5, # D2
                 1.0,  1.0, # C1
                 1.0,  0.5, # D1
                 0.5,  0.5, # D2
                ###
                 1.0,  1.0, # D1
                 0.5,  1.0, # D2
                 0.5,  0.5, # E2
                 1.0,  1.0, # D1
                 1.0,  0.5, # E1
                 0.5,  0.5, # E2
                ###
                 1.0,  1.0, # E1
                 0.5,  1.0, # E2
                 0.5,  0.5, # F2
                 1.0,  1.0, # E1
                 1.0,  0.5, # F1
                 0.5,  0.5, # F2
                ###
                 1.0,  1.0, # F1
                 0.5,  1.0, # F2
                 0.5,  0.5, # G2
                 1.0,  1.0, # F1
                 1.0,  0.5, # G1
                 0.5,  0.5, # G2
                ###
                 1.0,  1.0, # G1
                 0.5,  1.0, # G2
                 0.5,  0.5, # H2
                 1.0,  1.0, # G1
                 1.0,  0.5, # H1
                 0.5,  0.5, # H2
                ###
                 1.0,  1.0, # H1
                 0.5,  1.0, # H2
                 0.5,  0.5, # A2
                 1.0,  1.0, # H1
                 1.0,  0.5, # A1
                 0.5,  0.5, # A2


                 1.0,  1.0, # A3
                 0.5,  1.0, # A4
                 0.5,  0.5, # B4
                 1.0,  1.0, # A3
                 1.0,  0.5, # B3
                 0.5,  0.5, # B4
                ###
                 0.5,  0.5, # B3
                 0.0,  0.5, # B4
                 0.0,  0.0, # C4
                 0.5,  0.5, # B3
                 0.5,  0.0, # C3
                 0.0,  0.0, # C4
                ###
                 1.0,  1.0, # C3
                 0.5,  1.0, # C4
                 0.5,  0.5, # D4
                 1.0,  1.0, # C3
                 1.0,  0.5, # D3
                 0.5,  0.5, # D4
                ###
                 1.0,  1.0, # D3
                 0.5,  1.0, # D4
                 0.5,  0.5, # E4
                 1.0,  1.0, # D3
                 1.0,  0.5, # E3
                 0.5,  0.5, # E4
                ###
                 1.0,  1.0, # E3
                 0.5,  1.0, # E4
                 0.5,  0.5, # F4
                 1.0,  1.0, # E3
                 1.0,  0.5, # F3
                 0.5,  0.5, # F4
                ###
                 1.0,  1.0, # F3
                 0.5,  1.0, # F4
                 0.5,  0.5, # G4
                 1.0,  1.0, # F3
                 1.0,  0.5, # G3
                 0.5,  0.5, # G4
                ###
                 1.0,  1.0, # G3
                 0.5,  1.0, # G4
                 0.5,  0.5, # H4
                 1.0,  1.0, # G3
                 1.0,  0.5, # H3
                 0.5,  0.5, # H4
                ###
                 1.0,  1.0, # H3
                 0.5,  1.0, # H4
                 0.5,  0.5, # A4
                 1.0,  1.0, # H3
                 1.0,  0.5, # A3
                 0.5,  0.5, # A4

                 1.0,  1.0, # V2
                 0.5,  1.0, # V3
                 0.5,  0.5, # Y3
                 1.0,  1.0, # V2
                 1.0,  0.5, # Y2
                 0.5,  0.5, # Y3
                ###
                 1.0,  1.0, # Y2
                 0.5,  1.0, # Y3
                 0.5,  0.5, # X3
                 1.0,  1.0, # Y2
                 1.0,  0.5, # X2
                 0.5,  0.5, # X3
                ###
                 1.0,  1.0, # X2
                 0.5,  1.0, # X3
                 0.5,  0.5, # W3
                 1.0,  1.0, # X2
                 1.0,  0.5, # W2
                 0.5,  0.5, # W3
                ###
                 1.0,  1.0, # W2
                 0.5,  1.0, # W3
                 0.5,  0.5, # V3
                 1.0,  1.0, # W2
                 1.0,  0.5, # V2
                 0.5,  0.5, # V3
                
                 1.0,  1.0, # V4
                 0.5,  1.0, # V5
                 0.5,  0.5, # Y5
                 1.0,  1.0, # V4
                 1.0,  0.5, # Y4
                 0.5,  0.5, # Y5
                ###
                 1.0,  1.0, # Y4
                 0.5,  1.0, # Y5
                 0.5,  0.5, # X5
                 1.0,  1.0, # Y4
                 1.0,  0.5, # X4
                 0.5,  0.5, # X5
                ###
                 1.0,  1.0, # X4
                 0.5,  1.0, # X5
                 0.5,  0.5, # W5
                 1.0,  1.0, # X4
                 1.0,  0.5, # W4
                 0.5,  0.5, # W5
                ###
                 1.0,  1.0, # W4
                 0.5,  1.0, # W5
                 0.5,  0.5, # V5
                 1.0,  1.0, # W4
                 1.0,  0.5, # V4
                 0.5,  0.5, # V5


                 0.0,  1.0, # V5
                 0.5,  1.0, # W5
                 0.5,  0.5, # X5
                 0.0,  1.0, # V5
                 0.0,  0.5, # Y5
                 0.5,  0.5, # X5

                 0.5,  0.0, # K1
                 0.5,  0.5, # J1
                 1.0,  0.5, # J2
                 0.5,  0.0, # K1
                 1.0,  0.0, # K2
                 1.0,  0.5, # J2

                 0.5,  0.0, # K3
                 0.5,  0.5, # J3
                 1.0,  0.5, # J4
                 0.5,  0.0, # K3
                 1.0,  0.0, # K4
                 1.0,  0.5, # J4

                 0.5,  0.0, # N1
                 0.5,  0.5, # M1
                 1.0,  0.5, # M2
                 0.5,  0.0, # N1
                 1.0,  0.0, # N2
                 1.0,  0.5, # M2

                 0.5,  0.0, # N3
                 0.5,  0.5, # M3
                 1.0,  0.5, # M4
                 0.5,  0.0, # N3
                 1.0,  0.0, # N4
                 1.0,  0.5, # M4

            ])

            self.squareArrayBufferId = GL.glGenVertexArrays(1)
            GL.glBindVertexArray(self.squareArrayBufferId)
            GL.glEnableVertexAttribArray(0)
            GL.glEnableVertexAttribArray(1)
            
            idVertexBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idVertexBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(position)*position.itemsize, ctypes.c_void_p(position.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(0,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))

            idTextureBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idTextureBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(textureCoord)*textureCoord.itemsize, ctypes.c_void_p(textureCoord.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(1,2,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))
        

        GL.glUseProgram(self.pipeline1)
        GL.glBindVertexArray(self.squareArrayBufferId)
        projection = glm.perspective(math.pi/4,self.width/self.height,0.1,100)
        camera = glm.lookAt(glm.vec3(-25,10,15),glm.vec3(4,-9,7),glm.vec3(-5,-15,-10))
        model = glm.rotate(self.a,glm.vec3(0,0,1)) 
        mvp = projection * camera * model
        GL.glUniformMatrix4fv(GL.glGetUniformLocation(self.pipeline1, "MVP"),1,GL.GL_FALSE,glm.value_ptr(mvp))
        GL.glBindVertexArray(self.squareArrayBufferId)
        GL.glDrawArrays(GL.GL_TRIANGLES,0,294)
        self.a += 0.005

    

    def drawTerra(self):
        n = 50
        if self.sphereArrayBufferId == None:
            position = array('f')
            for i in range(0,n):
                theta = i*2*math.pi/n
                for j in range(0,n):
                    phi = j*math.pi/n-math.pi/2
                    position.append(math.cos(theta)*math.cos(phi))
                    position.append(math.sin(phi))
                    position.append(math.sin(theta)*math.cos(phi))

            self.sphereArrayBufferId = GL.glGenVertexArrays(1)
            GL.glBindVertexArray(self.sphereArrayBufferId)
            GL.glEnableVertexAttribArray(0)
            
            idVertexBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idVertexBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(position)*position.itemsize, ctypes.c_void_p(position.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(0,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))
        

        GL.glUseProgram(self.pipeline2)
        GL.glBindVertexArray(self.sphereArrayBufferId)
        projection = glm.perspective(math.pi/4,self.width/self.height,0.1,10)
        camera = glm.lookAt(glm.vec3(-2,-2.5,-1),glm.vec3(-0.7,-0.5,0),glm.vec3(0,0.5,0))
        model = glm.rotate(self.b,glm.vec3(0.1,-0.1,0))
        mvp = projection * camera * model
        GL.glUniformMatrix4fv(GL.glGetUniformLocation(self.pipeline2, "MVP"),1,GL.GL_FALSE,glm.value_ptr(mvp))
        GL.glDrawArrays(GL.GL_POINTS,0,n*n)
        self.b += 0.01

    def drawSpace(self):
        m = 100
        if self.sphereArrayBufferId == None:
            position = array('f')
            for i in range(0,m):
                theta = i*2*math.pi/m
                for j in range(0,m):
                    phi = j*math.pi/m-math.pi
                    position.append(math.cos(theta)*math.cos(phi))
                    position.append(math.sin(phi))
                    position.append(math.sin(theta)*math.cos(phi))

            self.sphereArrayBufferId = GL.glGenVertexArrays(1)
            GL.glBindVertexArray(self.sphereArrayBufferId)
            GL.glEnableVertexAttribArray(0)
            
            idVertexBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idVertexBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(position)*position.itemsize, ctypes.c_void_p(position.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(0,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))
        

        GL.glUseProgram(self.pipeline2)
        GL.glBindVertexArray(self.sphereArrayBufferId)
        projection = glm.perspective(math.pi/4,self.width/self.height,0.1,10)
        camera = glm.lookAt(glm.vec3(0,0,0),glm.vec3(0.1,0,0),glm.vec3(0,0.01,0))
        model = glm.rotate(self.c,glm.vec3(0,-0.1,0))
        mvp = projection * camera * model
        GL.glUniformMatrix4fv(GL.glGetUniformLocation(self.pipeline2, "MVP"),1,GL.GL_FALSE,glm.value_ptr(mvp))
        GL.glDrawArrays(GL.GL_POINTS,0,m*m)
        self.c += 0.001

        #pipeline
        #nave
        #star

    def draw(self):
        # clear screen and depth buffer
        GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)

        # Draw a Triangle
        self.drawTerra()
        self.drawSpace()
        self.drawSatelite()

SateliteF()