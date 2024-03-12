#import
import random
import tkinter as tk
from tkinter import simpledialog
#clases del proyecto
from CPais import CPais,IPais
from Visor import Visor
from Dado import Dado
from SimulationManager import SimulationManager
#loop jugable
prueba=CPais()
sim= SimulationManager(prueba)
eleccion=tk.simpledialog.askinteger("Elección", "¿Quieres crear una nueva simulación o cargar una existente?\n 1:cargar 2:nueva")
if eleccion==1:
    sim.cargar()
elif eleccion==2:
    num_paises=tk.simpledialog.askinteger("Número de paises", "Indica el número de paises")
    prueba.crear_paises(num_paises)
root=tk.Tk()
visor=Visor(root,sim)
elec=Dado(3)
# Schedule the first game round after a delay and start the GUI main loop
root.after(1000,lambda: sim.get_CPais().ronda(elec,root))
root.mainloop()