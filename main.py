#import
import random
import tkinter as tk
#clases del proyecto
from CPais import CPais,Pais
from Visor import Visor
from Dado import Dado
from SimulationManager import SimulationManager
#loop jugable
prueba=CPais()
root=tk.Tk()
visor=Visor(root,prueba)
elec=Dado(3)
sim= SimulationManager(prueba)
# Schedule the first game round after a delay and start the GUI main loop
sim.cargar()
root.after(1000,lambda: prueba.ronda(elec,root))
root.mainloop()