"""
    class Game
"""
import random
import requests
import json

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
            else:
                ret = self.__check(to_test)
        return ret

    def get_grid(self):
        """
            return grid
        """
        return self.grid

    def __check(self,word):
        """
            Private function to check is a word is a valid one
        """
        ret = False

        req = requests.get("https://wagon-dictionary.herokuapp.com/"+word)
        req_answer = req.json()
        ret = req_answer['found']

        return ret
