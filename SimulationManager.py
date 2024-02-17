class SimulationManager:
    def __init__(self,CPais):
        self.CPais=CPais
    def guardar(self):
        with open (".\guardados\guardado.txt","w") as f:
            info_paises="\n".join([f"{pais.get_id()},{pais.get_ext()}" for pais in self.CPais.get_paises()])
            f.write(info_paises)
    def cargar(self):
        #debe implementarse
        pass