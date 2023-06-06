# spritesheets.py
import pygame
from config import *

class Spritesheets:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()  # Load the spritesheet image file
        
    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])  # Create a new surface for the sprite
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))  # Copy the sprite region from the spritesheet onto the surface
        sprite.set_colorkey(BLACK)  # Set the transparent color key for the sprite
        return sprite  # Return the sprite surface
