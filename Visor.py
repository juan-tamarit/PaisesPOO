#imports
import tkinter as tk 
#clases del proyecto
from CPais import CPais, Pais
class Visor():
    def __init__(self, master, CPais):
        self.master=master
        self.CPais=CPais
        master.title("PaisesPOO V0.1")
        self.label=tk.Label(master,text=self.obt_info_paises())
        self.label.pack()
        self.master.after(1000, self.actualiza_info)
    def obt_info_paises(self):
        info_paises="\n".join([f"Pais ID:{pais.get_id()}, Ext:{pais.get_ext()}" for pais in self.CPais.get_paises()])
        return info_paises
    def actualiza_info(self):
        self.label.config(text=self.obt_info_paises())
        self.master.after(1000, self.actualiza_info)
