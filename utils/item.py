import pygame
from config import *

class Item:
    def __init__(self, name, image):
        self.name = name
        self.image = image
        
    def use(self):
        # Define What Happens When this item is used
        pass


class PokeBall(Item):
    def __init__(self, image):
        super().__init__("Poke-Ball", image)
        
    def use(self, creature):
        # Define what happens when a pokeball is used
        # This could be a simple capture or it could involve a capture chance based on the creatures stats
        return True # Return True if the capture is successful, False otherwise