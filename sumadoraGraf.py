#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
def suma():
	suma=int(entrada1.get())*int(entrada2.get())
	return var.set(suma)

ventana = tk.Tk()
ventana.title("Sumadora")
ventana.geometry('380x300')
ventana.configure(background = 'blue')
var = tk.StringVar()

e1 = tk.Label(ventana,text = "Numero 1: ",bg = "red",fg = "white")
e1.pack(padx = 5,pady = 5,ipadx = 5,ipady = 5,fill = tk.X)
entrada1 = tk.Entry(ventana)
entrada1.pack(fill = tk.X,padx = 80,pady = 5,ipadx = 2,ipady = 2)
e2 = tk.Label(ventana,text = "Numero 2: ",bg = "red",fg = "white")
e2.pack(padx = 5,pady = 5,ipadx = 5,ipady = 5,fill = tk.X)
entrada2 = tk.Entry(ventana)
entrada2.pack(fill = tk.X,padx = 80,pady = 5,ipadx = 2,ipady = 2)

btnsuma = tk.Button(ventana,text = "Suma",fg = "blue",command = suma)
btnsuma.pack(side = tk.TOP)

res = tk.Label(ventana,bg = "red",textvariable = var,padx = 5,pady = 5,width = 10)
res.pack()

ventana.mainloop()
