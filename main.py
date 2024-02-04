#import
import random
import os
#clases del proyecto
from CPais import CPais
from Dado import Dado
#fundiones del programa
def contienda(x,y):
    dado=Dado(10)
    x.atac(y,dado.rol())
    y.atac(x,dado.rol())
def mostrar(CPais):
    for pais in CPais.get_paises():
        print(pais.get_ext())
def limpia(CPais):
    for pais in CPais.get_paises():
        if pais.get_ext()<=0:
            CPais.remove_pais(pais)
def selec_objetivo(CPais,x):
    obj=random.randint(0,CPais.get_num_paises()-1)
    while(CPais.get_paises()[obj]==x):
        obj=random.randint(0,CPais.get_num_paises()-1)
    return CPais.get_paises()[obj]
#loop jugable
prueba=CPais()
prueba.crear_paises(10)
while (len(prueba.get_paises())>1):
    for pais in prueba.get_paises():
        contienda(pais,selec_objetivo(prueba,pais))
        limpia(prueba)
    mostrar(prueba)