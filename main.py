#import
import random
import tkinter as tk
#clases del proyecto
from CPais import CPais,Pais
from Visor import Visor
from Dado import Dado
#loop jugable
prueba=CPais()
prueba.crear_paises(3)
root=tk.Tk()
visor=Visor(root,prueba)
elec=Dado(3)
# Schedule the first game round after a delay and start the GUI main loop
root.after(1000,lambda: prueba.ronda(elec,root))
root.mainloop()