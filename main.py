from CPais import CPais
import random
def contienda(CPais,x,y):
    CPais.get_pais_by_id(x).atac(CPais.get_pais_by_id(y))
    CPais.get_pais_by_id(y).atac(CPais.get_pais_by_id(x))
def mostrar(CPais):
    for pais in CPais.get_paises():
        print(pais.get_ext())
prueba=CPais()
prueba.crear_paises(2)
mostrar(prueba)
contienda(prueba,0,1)
mostrar(prueba)
