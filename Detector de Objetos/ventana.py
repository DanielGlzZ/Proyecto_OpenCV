from tkinter import *
from reloj import Reloj
from palma import Palma
from camion import Camion
from  muneca import Muneca

class Ventana:
    def __init__(self):

        raiz = Tk()

        #Modificación de la ventana

        raiz.title("Reconocimiento de Objetos") #Modificar el titulo

        # raiz.resizable(0,0) #Este es para redimensionar la ventana

        raiz.iconbitmap("detector-de-rostros.ico") #Asignar un icono a la venta

            # raiz.geometry("750x450") #Tamaño de la ventana

        raiz.config(bg="#323") #Asigar color a la ventana

        raiz.config(bd="10")

        raiz.config(relief="sunken")

        raiz.config(cursor="hand2")

            #Creación del Frame

        miFrame = Frame() #Creación del Frame

            # miFrame.pack(fill="both", expand="true") #Con esto se puede expandir

        miFrame.pack()

        miFrame.config(bg="#323") #Damos color al Frame

        miFrame.config(width="650", height="350") #Se debe dar medidas al Frame y la Raiz toma estas medidas

        miFrame.config(bd="10")

        miFrame.config(relief="sunken")

        miFrame.config(cursor="pirate")

            #Label que muestra el titulo

        miLabel = Label(miFrame, text="Reconocimiento de Objetos", font=("Comic Sans MS",18))

        miLabel.place(x=160, y=20)

            #Imagen y escalado

            #Primer Imagen
        miPalmaImagen = PhotoImage(file = "palma.png")

        miPalmaImagenR = miPalmaImagen.subsample(5)

            #Segunda Imagen 
        miCamionImagen = PhotoImage(file = "camion.png")

        miCamionImagenR = miCamionImagen.subsample(5)

            #Tercer Imagen 
        miMunecaImagen = PhotoImage(file = "muneca.png")

        miMunecaImagenR = miMunecaImagen.subsample(5)

            #Cuarta Imagen 
        miRelojImagen = PhotoImage(file = "reloj.png")

        miRelojImagenR = miRelojImagen.subsample(5)

            #Creacion de los botones

            #Primer boton "Palma"
            
                

        botonPalma = Button(raiz, image =  miPalmaImagenR, command=Palma, height="112.5", width="112.5") #Boton con una funcion que vuelve una imagen de otro tamaño

        botonPalma.place(x=40,y=200)

            #Segundo boton "Palma"
        botonCamion = Button(raiz, image = miCamionImagenR, command=Camion,height="112.5", width="112.5") 

        botonCamion.place(x=192.5,y=200)

            #Tercer boton "Muñeca"
        botonMuneca = Button(raiz, image = miMunecaImagenR, command=Muneca, height="112.5", width="112.5") 

        botonMuneca.place(x=345,y=200) 

            #Tercer boton "Reloj"
        botonReloj = Button(raiz, image = miRelojImagenR, command=Reloj, height="112.5", width="112.5") 

        botonReloj.place(x=497.5,y=200)

        raiz.mainloop() #Este metodo siempre al final xd

Ventana()