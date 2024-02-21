#imports
import tkinter as tk 
#clases del proyecto
from ICPais import ICPais
#clase
class Visor():
    """
    Provides a graphical interface to display information about countries in the game.

    Attributes:
    - master (tk.Tk): The main window of the GUI.
    - CPais (CPais): An instance of CPais containing country information.

    Methods:
    - __init__(master, CPais): Initializes the Visor with the given master window and CPais instance.
    - obt_info_paises(): Obtains formatted information about countries from CPais.
    - actualiza_info(): Updates the displayed information periodically.
    """
    def __init__(self, master, ICPais):
        """
        Initializes the Visor with the given master window and CPais instance.

        Parameters:
        - master (tk.Tk): The main window of the GUI.
        - CPais (CPais): An instance of CPais containing country information.
        """
        self.master=master
        self.ICPais=ICPais
        master.title("PaisesPOO V0.1")
        self.label=tk.Label(master,text=self.obt_info_paises())
        self.label.pack()
        self.master.after(1000, self.actualiza_info)
    def obt_info_paises(self):
        """
        Obtains formatted information about countries from CPais.

        Returns:
        - str: Formatted information about countries.
        """
        info_paises="\n".join([f"Pais ID:{pais.get_id()}, Ext:{pais.get_ext()}" for pais in self.ICPais.get_paises()])
        return info_paises
    def actualiza_info(self):
        """
        Updates the displayed information periodically.
        """
        self.label.config(text=self.obt_info_paises())
        self.master.after(1000, self.actualiza_info)
