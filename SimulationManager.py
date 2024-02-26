#clases del proyecto
from Pais import Pais
from ISim import ISim
#clase
class SimulationManager(ISim):
    """
    Manages the simulation state, providing methods for saving and loading country information.

    Attributes:
    - CPais (CPais): The CPais object representing the collection of countries.

    Methods:
    - __init__(CPais): Initializes a SimulationManager instance with a CPais object.
    - guardar(): Saves the simulation state to a text file.
    - cargar(): Loads the simulation state from a text file.
    """
    def __init__(self,ICPais):
        """
        Initializes a SimulationManager instance.

        Parameters:
        - CPais (CPais): The CPais object representing the collection of countries.
        """
        self.ICPais=ICPais
    def get_CPais(self):
        return self.ICPais
    def set_CPais(self,ICPais):
        self.ICPais=ICPais
    def guardar(self):
        """
        Saves the simulation state to a text file.

        This method creates a text file ("guardado.txt") in the "./guardados/" directory
        and writes the information of each country (ID and external state) in the CPais object
        to the file in the format "ID,EXT", with each country on a new line.
        """
        with open (".\guardados\guardado.txt","w") as f:
            info_paises="\n".join([f"{pais.get_id()},{pais.get_ext()}" for pais in self.ICPais.get_paises()])
            f.write(info_paises)
    def cargar(self):
        """
        Loads the simulation state from a text file.

        This method reads the "guardado.txt" file from the "./guardados/" directory,
        extracts information for each country (ID and external state), creates Pais objects,
        and sets the CPais object's list of countries to the loaded data.
        """
        paises=[]
        with open(".\guardados\guardado.txt","r") as f:
            for line in f.readlines():
                info=line.split(",")
                pais=Pais(int(info[0]))
                pais.set_ext(int(info[1]))
                paises.append(pais)
        self.ICPais.set_paises(paises)