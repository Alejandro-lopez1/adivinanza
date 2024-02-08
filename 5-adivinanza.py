import tkinter as tk 
from tkinter import messagebox
import random

class JuegoAdivinanzaApp:
    def __init__(self, master):
        self.master = master
        self.master.title=("Juego de Adivinanzas")

        #generamos un número aleatorio entre 1 y 100
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

        #etiqueta para mostar instrucciones
        self.instrucciones_label = tk.Label(self.master, text= "Estoy pensando en un número del 1 al 100")
        self.instrucciones_label.pack()

        #entrada de texto para que el usuario ingrese su suposición
        self.suposicion_entry = tk.Entry(self.master)
        self.suposicion_entry.pack()

        #botón para enviar la suposicion del usuario
        self.enviar_button = tk.Button(self.master, text="Adivinar", command=self.verificar_suposicion)
        self.enviar_button.pack()

    def verificar_suposicion(self):
        #obtiene la suposicion del usuario
        suposicion = int(self.suposicion_entry.get())#convertimos la variable de str a int

        '''# Intenta convertir la suposición a un entero
        try:
            suposicion = int(suposicion_str)
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un número válido.")
        return'''
    
        #incrementa el contadro de intentos
        self.intentos += 1

        #compara la suposicion del usuario con el numero secreto
        if suposicion < self.numero_secreto:
            messagebox.showinfo("Adivinanza", "Demasiado bajo. Intenta nuevamente.")
        elif suposicion > self.numero_secreto:
            messagebox.showinfo("Adivinanza", "Demasiado alto. Intenta nuevamente.")
        else:
            messagebox.showinfo("¡Felicidades!", f"Adivinaste el número en {self.intentos} intentos")
            self.master.quit() #cierra la ventana cuando el usuario adivina correctamente

if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoAdivinanzaApp(root)
    root.mainloop()