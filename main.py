#import
import random
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
            print ("El pais ",pais.get_id()," ha desaparecido")
            CPais.remove_pais(pais)
def selec_objetivo(CPais,x):
    obj_id=random.randint(0,len(prueba.get_paises())-1)
    while(obj_id==x):
        obj_id=random.randint(0,len(prueba.get_paises())-1)
    return CPais.get_pais_by_id(obj_id)
prueba=CPais()
prueba.crear_paises(2)
while (len(prueba.get_paises())>1):
    contienda(prueba.get_pais_by_id(0),prueba.get_pais_by_id(1))
    mostrar(prueba)
    limpia(prueba)
