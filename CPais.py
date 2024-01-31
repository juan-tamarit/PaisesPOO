from Pais import Pais
class CPais():
    def __init__(self):
        self.paises=[]
    def crear_paises(self,n):
        for i in range(n):
            aux=Pais(i)
            self.get_paises().append(aux)
    def get_paises(self):
        return self.paises
    def set_paises(self, paises):
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
            elif self.get_paises()[len((self.get_paises())-1)-cont].get_id()==id:
                sol=self.get_paises()[len((self.get_paises())-1)-cont]
                found=True
            cont+=1
        return sol