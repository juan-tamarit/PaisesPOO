#import
import random
import tkinter as tk
#clases del proyecto
from CPais import CPais,Pais
from Visor import Visor
from Dado import Dado
#fundiones del programa
def contienda(x,y):
    """
    Simulates a conflict between two countries, adjusting their external states based on random dice rolls.

    Parameters:
    - x (Pais): The attacking country.
    - y (Pais): The defending country.
    """
    dado=Dado(10)
    x.atac(y,dado.rol())
    y.atac(x,dado.rol())
def cura(x):
    """
    Simulates healing a country, increasing its external state based on a random dice roll.

    Parameters:
    - x (Pais): The country to be healed.
    """
    dado=Dado(5)
    x.heal(dado.rol())
def enviar_ayuda(x,y):
    """
    Simulates sending aid from one country to another, adjusting their external states based on a random dice roll.

    Parameters:
    - x (Pais): The country sending aid.
    - y (Pais): The country receiving aid.
    """
    dado=Dado(10)
    x.ayuda(y,dado.rol())
def limpia(CPais):
    """
    Cleans up countries with external states less than or equal to 0 from the list.

    Parameters:
    - CPais (CPais): The collection of countries.
    """
    for pais in CPais.get_paises():
        if pais.get_ext()<=0:
            CPais.remove_pais(pais)
def selec_objetivo(CPais,x):
    """
    Selects a random country as a target, excluding the provided country.

    Parameters:
    - CPais (CPais): The collection of countries.
    - x (Pais): The country to be excluded from selection.

    Returns:
    - Pais: The selected target country.
    """
    obj=random.randint(0,CPais.get_num_paises()-1)
    while(CPais.get_paises()[obj]==x):
        obj=random.randint(0,CPais.get_num_paises()-1)
    return CPais.get_paises()[obj]
def ronda (CPais,Dado,root):
    """
    Simulates a game round, where each country in CPais takes a random action.

    Parameters:
    - CPais (CPais): The collection of countries.
    - Dado (Dado): The dice used to determine actions.
    - root (tk.Tk): The main window of the GUI.
    """
    for pais in CPais.get_paises():
        elec_aux=Dado.rol()
        if elec_aux==1:
            contienda(pais,selec_objetivo(CPais,pais))
        elif elec_aux==2:
            if pais.get_ext()<=80:
                cura(pais)
            else:
                contienda(pais,selec_objetivo(CPais,pais))
        elif elec_aux==3:
            enviar_ayuda(pais,selec_objetivo(CPais,pais))
        limpia(CPais)
    root.after(1000,lambda: ronda(prueba,elec,root))
#loop jugable
prueba=CPais()
prueba.crear_paises(3)
root=tk.Tk()
visor=Visor(root,prueba)
elec=Dado(3)
# Schedule the first game round after a delay and start the GUI main loop
root.after(1000,lambda: ronda(prueba,elec,root))
root.mainloop()