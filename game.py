"""
    class Game
"""
import random

class Game():
    """
        class Game
    """

    def __init__(self):
        """
            __init__ function
        """

        ## A-Z => 65-90
        self.grid = [chr(random.randint(ord('A'), ord('Z'))) for x in range(0, 9)]

    def is_valid(self, to_test):
        """
            is_valid
        """
        ret = True
        if len(to_test) == 0:
            ret = False
        for letter in to_test:
            if letter not in self.grid:
                ret = False
        return ret

    def get_grid(self):
        """
            return grid
        """
        return self.grid
