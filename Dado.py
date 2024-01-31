import random
class Dado():
    def __init__(self,max):
        """
        Initialize a dice with a specified maximum value.

        Parameters:
        - max (int): The maximum value that the dice can roll.
        """
        self.max=max
    def get_max(self):
        """
        Retrieve the maximum value of the dice.

        Returns:
        - int: The maximum value that the dice can roll.
        """
        return self.max
    def set_max(self,max):
        """
        Set the maximum value of the dice.

        Parameters:
        - max (int): The new maximum value for the dice.
        """
        self.max=max
    def rol(self):
        """
        Roll the dice and return a random value between 1 and the maximum value.

        Returns:
        - int: A random value representing the result of the dice roll.
        """
        return random.randint(1,self.max)