import random
class Pais():
    def __init__(self,id):
        self.id=id
        self.ext=100
    def get_id(self):
        return self.id
    def set_id(self,id):
        self.id=id
    def get_ext (self):
        return self.ext
    def set_ext(self,ext):
        self.ext=ext
    def atac(self,other):
        """
        Attack another country, modifying their 'ext' attribute based on a random value.

        Parameters:
        - other (Pais): Another country to be attacked.

        The 'atac' method simulates an attack between two countries. A random integer
        between 0 and 10 is generated, representing the intensity of the attack. The
        'ext' attribute of the attacked country ('other') is then reduced by this random
        value, while the 'ext' attribute of the attacking country (self) is increased
        by the same value.
        """
        aux=random.randint(0,10)
        other.set_ext(other.get_ext()-aux)
        self.set_ext(self.get_ext()+aux)