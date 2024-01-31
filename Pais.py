class Pais():
    """
    Represents a country with an identifier and an external state (ext).

    Attributes:
    - id (int): Unique identifier for the country.
    - ext (int): External state or health of the country, initialized to 100.

    Methods:
    - get_id(): Retrieve the country's identifier.
    - set_id(id): Set a new identifier for the country.
    - get_ext(): Retrieve the current external state of the country.
    - set_ext(ext): Set a new external state for the country.
    - atac(other, value): Simulate an attack on another country, adjusting their
      external state based on the specified value.
    - heal(value): Increase the country's external state by the specified value.
    """
    def __init__(self,id):
        """
        Initialize a country with the given identifier.

        Parameters:
        - id (int): Unique identifier for the country.
        """
        self.id=id
        self.ext=100
    def get_id(self):
        """
        Retrieve the identifier of the country.

        Returns:
        - int: The unique identifier of the country.
        """
        return self.id
    def set_id(self,id):
        self.id=id
        """
        Set a new identifier for the country.

        Parameters:
        - id (int): The new unique identifier for the country.
        """
    def get_ext (self):
        """
        Retrieve the current external state of the country.

        Returns:
        - int: The current external state or health of the country.
        """
        return self.ext
    def set_ext(self,ext):
        """
        Set a new external state for the country.

        Parameters:
        - ext (int): The new external state or health for the country.
        """
        self.ext=ext
    def atac(self,other,value):
        """
        Simulate an attack on another country, adjusting their external state
        based on the specified value.

        Parameters:
        - other (Pais): Another country object to be attacked.
        - value (int): The intensity of the attack, affecting the external state.
        """
        other.set_ext(other.get_ext()-value)
        self.set_ext(self.get_ext()+value)
    def heal(self,value):
        """
        Increase the country's external state by the specified value.

        Parameters:
        - value (int): The amount by which to increase the country's external state.
        """
        self.set_ext(self.get_ext()+value)