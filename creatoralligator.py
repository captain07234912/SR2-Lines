from Render import Render, color


########################### Lista de colores para probar
Fondo = color(0,0,0) #negro
Blanco = color(1,1,1)
CYAN = color(0,1,1)
Red = color(1,0,0)
BLUE = (0,0,1)
YELLOW = (1,1,0)

###########################################################
# tamaño de la imagen
prueba = Render(1000, 1000)
# introduzca el tamaño del viewport
prueba.glViewport(250, 250, 600, 600)

# ingrese el color del fondo
prueba.glClearColor(0,0,0)

# ingrese el color para pintar
prueba.glColor(1, 0, 0)
prueba.glClear()

######################Punto ##################################
# si quiere pintar un punto es aqui
#prueba.punto(150,275)
#prueba.glColor(1,0,0)
#prueba.punto(100,200)

# quiere pintar una linea, perfecto! aca es el espacio
prueba.glLinea(-1,1, 1,-1)
prueba.glLinea(-1,-1,1,1)
prueba.glLinea(1,0,-1,-1)
prueba.glLinea(1,-1,1,1)



prueba.glFinish('LineaPrueba.bmp')



