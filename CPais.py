import random
#clases del proyecto
from IPais import IPais
from Dado import Dado
#clase
class CPais():
    """
    Represents a collection of countries with methods to manage and retrieve country information.

    Attributes:
    - paises (list): A list to store instances of the Pais class.

    Methods:
    - __init__(): Initializes CPais with an empty list of countries.
    - crear_paises(n): Creates and appends 'n' country instances to the list.
    - get_paises(): Retrieves the list of countries.
    - set_paises(paises): Sets the list of countries to the provided list.
    - get_pais_by_id(id): Retrieves a country by its unique ID from the list of countries.
    - remove_pais(Pais): Removes a country from the list of countries.
    - get_num_paises(): Gets the number of countries in the CPais object.
    - contienda(other): Simulates a conflict between two countries.
    - cura(): Simulates healing a country.
    - enviar_ayuda(other): Simulates sending aid from one country to another.
    - limpia(): Cleans up countries with external states less than or equal to 0 from the list.
    - selec_objetivo(): Selects a random country as a target, excluding the current country.
    - ronda(Dado, root): Simulates a game round, where each country takes a random action.
    """
    def __init__(self):
        """
        Initializes CPais with an empty list of countries.
        """
        self.paises=[]
    def crear_paises(self,n):
        """
        Creates and appends 'n' country instances to the list.

        Parameters:
        - n (int): The number of country instances to create.
        """
        for i in range(n):
            aux=IPais(i)
            self.get_paises().append(aux)
    def get_paises(self):
        """
        Retrieves the list of countries.

        Returns:
        - list: A list of country instances.
        """
        return self.paises
    def set_paises(self, paises):
        """
        Sets the list of countries to the provided list.

        Parameters:
        - paises (list): A list of country instances.
        """
        self.paises=paises
    def get_pais_by_id(self,id):
        """
        Retrieve a country by its ID from the list of countries.

        Parameters:
        - id (int): The unique identifier of the country to retrieve.

        Returns:
        - Country: The Country object with the specified ID, or None if not found.

        The function iterates through the list of countries in their original order
        and then in reverse order, stopping as soon as it finds a country with the
        specified ID. Returns the corresponding Country object or None if no match is found.
        """
        sol=None
        cont=0
        found=False
        while cont<=len(self.get_paises())//2 and not found:
            if self.get_paises()[cont].get_id()==id:
                sol=self.get_paises()[cont]
                found=True
            elif self.get_paises()[len(self.get_paises())-1-cont].get_id()==id:
                sol=self.get_paises()[len(self.get_paises())-1-cont]
                found=True
            cont+=1
        return sol
    def remove_pais(self, Pais):
        """
        Remove a country from the list of countries.

        Parameters:
        - pais (Pais): The country object to be removed from the list.

        This method removes the specified country from the list of countries in CPais.
        It uses the `remove` method, which eliminates the first occurrence of the
        provided country object based on its value, not its index.

        Note:
        If there are multiple occurrences of the country object in the list,
        only the first occurrence will be removed.
        """
        self.paises.remove(IPais)
    def get_num_paises(self):
        """
        Get the number of countries in the CPais object.

        Returns:
        - int: The total number of countries in the CPais object.

        This method provides the count of countries currently present in the CPais object.
        It uses the `len` function to determine the length of the internal list of countries.
        """
        return len(self.get_paises())
    def contienda(self,x,y):
        """
        Simulates a conflict between two countries, adjusting their external states based on random dice rolls.

        Parameters:
        - x (Pais): The attacking country.
        - y (Pais): The defending country.
        """
        dado=Dado(10)
        x.atac(y,dado.rol())
        y.atac(x,dado.rol())
    def cura(self,x):
        """
        Simulates healing a country, increasing its external state based on a random dice roll.

        Parameters:
        - x (Pais): The country to be healed.
        """
        dado=Dado(5)
        x.heal(dado.rol())
    def enviar_ayuda(self,x,y):
        """
        Simulates sending aid from one country to another, adjusting their external states based on a random dice roll.

        Parameters:
        - x (Pais): The country sending aid.
        - y (Pais): The country receiving aid.
        """
        dado=Dado(10)
        x.ayuda(y,dado.rol())
    def limpia(self):
        """
        Cleans up countries with external states less than or equal to 0 from the list.

        Parameters:
        - self (CPais): The collection of countries.
        """
        for pais in self.get_paises():
            if pais.get_ext()<=0:
                self.remove_pais(pais)
    def selec_objetivo(self,x):
        """
        Selects a random country as a target, excluding the provided country.

        Parameters:
        - self (CPais): The collection of countries.
        - x (Pais): The country to be excluded from selection.

        Returns:
        - Pais: The selected target country.
        """
        obj=random.randint(0,self.get_num_paises()-1)
        while(self.get_paises()[obj]==x):
            obj=random.randint(0,self.get_num_paises()-1)
        return self.get_paises()[obj]
    def ronda (self,Dado,root):
        """
        Simulates a game round, where each country in CPais takes a random action.

        Parameters:
        - self (CPais): The collection of countries.
        - Dado (Dado): The dice used to determine actions.
        - root (tk.Tk): The main window of the GUI.
        """
        for pais in self.get_paises():
            elec_aux=Dado.rol()
            if elec_aux==1:
                self.contienda(pais,self.selec_objetivo(pais))
            elif elec_aux==2:
                if pais.get_ext()<=80:
                    self.cura(pais)
                else:
                    self.contienda(pais,self.selec_objetivo(pais))
            elif elec_aux==3:
                self.enviar_ayuda(pais,self.selec_objetivo(pais))
            self.limpia()
        root.after(1000,lambda: self.ronda(Dado,root))