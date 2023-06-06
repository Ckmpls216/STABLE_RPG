# tallgrass.py
import pygame
from config import *


class TallGrass(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game  # Store a reference to the game instance
        self._layer = GRASS_LAYER  # Set the layer for sprite ordering
        self.groups = self.game.all_sprites  # Assign the sprite groups to which the object belongs
        pygame.sprite.Sprite.__init__(self, self.groups)  # Initialize the sprite base class
        
        self.x = x * TILESIZE  # Calculate the x-coordinate of the ground tile
        self.y = y * TILESIZE  # Calculate the y-coordinate of the ground tile
        self.width = TILESIZE  # Set the width of the ground tile
        self.height = TILESIZE  # Set the height of the ground tile
        
        self.image = self.game.terrain_spritesheet.get_sprite(540, 352, self.width, self.height)  # Load the sprite image for the ground tile
        
        self.rect = self.image.get_rect()  # Get the rectangle that encloses the ground tile image
        self.rect.x = self.x  # Set the x-coordinate of the ground tile rectangle
        self.rect.y = self.y  # Set the y-coordinate of the ground tile rectangle