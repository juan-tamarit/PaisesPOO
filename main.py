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
sim= SimulationManager(prueba)
root=tk.Tk()
visor=Visor(root,sim.get_CPais())
elec=Dado(3)

# Schedule the first game round after a delay and start the GUI main loop
sim.cargar()
root.after(1000,lambda: sim.get_CPais().ronda(elec,root))
root.mainloop()