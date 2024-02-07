#clases del proyecto
from Pais import Pais
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
            aux=Pais(i)
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
        self.paises.remove(Pais)
    def get_num_paises(self):
        """
        Get the number of countries in the CPais object.

        Returns:
        - int: The total number of countries in the CPais object.

        This method provides the count of countries currently present in the CPais object.
        It uses the `len` function to determine the length of the internal list of countries.
        """
        return len(self.get_paises())