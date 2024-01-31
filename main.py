from CPais import CPais
from Dado import Dado
def contienda(CPais,x,y):
    dado=Dado(10)
    CPais.get_pais_by_id(x).atac(CPais.get_pais_by_id(y),dado.rol())
    CPais.get_pais_by_id(y).atac(CPais.get_pais_by_id(x),dado.rol())
def mostrar(CPais):
    for pais in CPais.get_paises():
        print(pais.get_ext())
prueba=CPais()
prueba.crear_paises(2)
mostrar(prueba)
contienda(prueba,0,1)
mostrar(prueba)
