# block.py
import pygame
from config import *

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game  # Store a reference to the game instance
        self._layer = BLOCK_LAYER  # Set the layer for sprite ordering
        self.groups = self.game.all_sprites, self.game.blocks  # Assign the sprite groups to which the object belongs
        pygame.sprite.Sprite.__init__(self, self.groups)  # Initialize the sprite base class
        
        self.x = x * TILESIZE  # Calculate the x-coordinate of the block
        self.y = y * TILESIZE  # Calculate the y-coordinate of the block
        self.width = TILESIZE  # Set the width of the block
        self.height = TILESIZE  # Set the height of the block
        
        self.image = self.game.terrain_spritesheet.get_sprite(960, 448, self.width, self.height)  # Load the sprite image for the block
        
        self.rect = self.image.get_rect()  # Get the rectangle that encloses the block image
        self.rect.x = self.x  # Set the x-coordinate of the block rectangle
        self.rect.y = self.y  # Set the y-coordinate of the block rectangle
        


class Water(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = WATER_LAYER
        self.groups = self.game.all_sprites, self.game.blocks 
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(864, 160, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
