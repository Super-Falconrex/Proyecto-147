# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:51:49 2023


@author: Samuel
"""


from tkinter import * #importando tkinter


root = Tk()


root.title("Fibonacci") #titulo de ventana
root.geometry("400x400") #tamaño de ventana


label_series = Label(root, text="Serie Fibonacci:  ")
label_suma = Label(root)



def Fibonacci(): #defino funcion
    num = 10
    first = 0 
    second = 1 
    sum = 0
    counter = 1
    while (counter <= num):
        #sum contiene la serie Fibonacci
        #str convierte el valor a cadena
        label_series["text"] += str(sum) + " "
        counter = counter + 1
        first = second
        second = sum
        sum = first + second
    #mostrar los textos en etiquetas    
    label_suma["text"] = "El total de espirales es  " + str(sum)

ipt = input(root)
btn = Button(root, text="Mostrar la serie Fibonacci", command=Fibonacci)


#para que se muestren mis componentes (etiquetas, botones)
ipt.pack()
btn.pack()
label_series.pack()
label_suma.pack()


root.mainloop()#obligatoria para ejecutar
