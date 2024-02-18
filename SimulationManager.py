from Pais import Pais
class SimulationManager:
    def __init__(self,CPais):
        self.CPais=CPais
    def guardar(self):
        with open (".\guardados\guardado.txt","w") as f:
            info_paises="\n".join([f"{pais.get_id()},{pais.get_ext()}" for pais in self.CPais.get_paises()])
            f.write(info_paises)
    def cargar(self):
        paises=[]
        with open(".\guardados\guardado.txt","r") as f:
            for line in f.readlines():
                info=line.split(",")
                pais=Pais(int(info[0]))
                pais.set_ext(int(info[1]))
                paises.append(pais)
        self.CPais.set_paises(paises)
                