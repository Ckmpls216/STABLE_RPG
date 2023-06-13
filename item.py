import pygame
import random
from utils.config import *

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
        
class PokeBall(Item):
    def __init__(self):
        super().__init__("Poke Ball", "A Device For Catching Wild Creatures.")
        self.image = pygame.image.load('img/pokeBall.png')
        
        
        
    def use(self, creature):
        # add logic here to try and catch the creatures
        # 50% chance to catch the creature
        if random.random() < 0.5:
            print(f"You Caught the {creature.name}!")
            return True
        
        else:
            print(f"The {creature.name} escaped!")
            return False