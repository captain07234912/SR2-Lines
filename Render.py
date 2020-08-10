import struct
from LibreriaGL import *

"""
Universidad del Valle de Guatemala
Graficas por computadora
Render
Jorge Suchite Carnet 15293
07/07/2020
SR2 : Lines
"""



class Render(object):
    def __init__(self, width, height):
        self.colorPintar = YELLOW
        self.Fondo = Fondo
        self.glCreateWindow(width, height)
        # ancho y largo de la imagen

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()
        #tamani exacto de la ventana
        self.glViewport(0, 0, width, height)

    """
    define el area  de la imagen sobre la que vas a dibujar
    """
    def glViewport(self, x, y, width, height):
        self.CoorxViewport = x
        self.CooryViewport = y
        self.ViewportHEight = height
        self.ViewportWidth = width

    """funcion que llena toda la imagen de un solo color con pixeles   
         tomando la imagen como una matriz papu"""
    def glClear(self):
        self.pixels = [[self.Fondo for x in range(self.width)] for y in range(self.height)]

    # funcion que me deeja ahcer el punto x largo y  alto
    def punto(self,x,y):
        self.pixels[y][x] = self.colorPintar

    """ https://www.khronos.org/registry/OpenGL-Refpages/es2.0/xhtml/glViewport.xml
    
        link donde se utilizo la formula para el viewport"""
    # vertex relativo al viewport punto en pantalla conversion valor en pixel
    def glVertex(self, x, y):
        pixelX =  int(( x + 1) * (self.ViewportWidth / 2) + self.CoorxViewport)
        pixelY =  int(( y + 1) * (self.ViewportHEight / 2) + self.CooryViewport)
        self.pixels[pixelY][pixelX] = self.colorPintar
    def glvertexLinea(self,xcoor,ycoor):
        self.pixels[ycoor][xcoor] =self.colorPintar


    # j balvin men
    # este colores me sirve para guardar el color
    def glColor(self, r, g, b):
        self.colorPintar = color(r, g, b)
    # poner el color de fondo si quiere cuas

    def glClearColor(self, r, g, b):
        self.Fondo = color(r, g, b)
    # funcion que me deja escribir el BMP

    # aca termina lo de puntos

    ############################ Lineas
    ## algoritmo de bresenham dibujar una linea
    """https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm"""

    def glLinea(self, xi, yi, xn, yn ):
        # coordenadas iniciales y siguientes

        xi = round((xi+1) * (self.ViewportWidth/2 ) + self.CoorxViewport)
        yi = round((yi +1) * (self.ViewportHEight /2 ) + self.CooryViewport)
        xn = round((xn+1) * (self.ViewportWidth / 2) + self.CoorxViewport)
        yn = round((yn +1) * (self.ViewportHEight / 2 ) + self.CooryViewport)

    # distancias que se desplazan en cada eje calculando pendiente
        distx = abs(xn -xi)
        disty = abs(yn -yi)
        inclinacion = disty > distx
    # valores inclinados o rectos de 0 a 1

        if inclinacion:

            xi,yi = yi,xi
            xn,yn = yn,xn

        if xi > xn:
            xi,xn =xn,xi
            yi, yn = yn, yi

        distx = abs(xn-xi)

        disty = abs(yn -yi)

        moving = 0
        limite = 0.5
        m = disty/distx
        ycoor = yi

        for xcoor in range(xi, xn + 1):
            if inclinacion:
                self.glvertexLinea(ycoor,xcoor)
            else:
                self.glvertexLinea(xcoor,ycoor)

            moving += m
            if moving >= limite:
                ycoor += 1 if yi < yn else -1
                limite += 1





    def glFinish(self, filename):
        archivo = open(filename, 'wb')

        # header del archivo de  14 bytes
        archivo.write(bytes('B'.encode('ascii')))
        archivo.write(bytes('M'.encode('ascii')))
        archivo.write(dword(14 + 40 + self.width * self.height * 3))
        archivo.write(dword(0))
        archivo.write(dword(14 + 40))

        # header del Mitmap de 40 bytes
        archivo.write(dword(40))
        archivo.write(dword(self.width))
        archivo.write(dword(self.height))
        archivo.write(word(1))
        archivo.write(word(24))
        archivo.write(dword(0))
        archivo.write(dword(self.width * self.height * 3))
        archivo.write(dword(0))
        archivo.write(dword(0))
        archivo.write(dword(0))
        archivo.write(dword(0))


        for x in range(self.height):
            for y in range(self.width):
                archivo.write(self.pixels[x][y])

        archivo.close()









                











