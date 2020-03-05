import tkinter as tk
win = tk.Tk()
# Code to add widgets will go here...
# tk.[widgetname](root window, properties/configuration);
campoDeTexto = tk.Entry(win)
campoDeTexto.pack()

boton = tk.Button(win,text = "Insertar")
boton.pack()


win.mainloop()