import pygame
from map.block import *
from utils.config import *
from map.ground import *
from map.dirtpath import DirtPath
from characters.player import *
from utils.spritesheets import *
from map.tallgrass import *
from map.tilemap import *
from item import Item, PokeBall
import sys
import random


class Inventory:
    def __init__(self):
        self.items = []  # List to store items

    def add_item(self, item):
        self.items.append(item)  # Add item to the list

    def remove_item(self, item):
        self.items.remove(item)  # Remove item from the list

    def has_item(self, item):
        return item in self.items  # Check if item exists in the list


class PlayerInventory:
    def __init__(self):
        self.inventory = Inventory()  # Player's inventory


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        # Load in Spritesheets
        self.character_spritesheet = Spritesheets('img/character.png')  # Load the spritesheet for the character
        self.terrain_spritesheet = Spritesheets('img/terrain.png')  # Load the spritesheet for the terrain

        self.playerInventory = PlayerInventory()  # Reference to the player inventory instance

    def createTilemap(self):
        # Create the tilemap for the game world
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)  # Create ground tiles
                if column == "B":
                    Block(self, j, i)  # Create block tiles
                if column == "W":
                    Water(self, j, i)
                if column == "P":
                    self.player = Player(self, j, i)  # Create the player character
                if column == "T":
                    TallGrass(self, j, i)  # Create enemy characters
                if column == "x":
                    DirtPath(self, j, i)

    def new(self):
        # Start a new game
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTilemap()

    def events(self):
        # Handle game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        # Update the game state
        self.all_sprites.update()

    def draw(self):
        # Draw the game on the screen
        self.screen.fill(BLACK)

        # Calculate the offset to center the player sprite
        player_offset_x = (WIN_WIDTH // 2) - self.player.rect.centerx
        player_offset_y = (WIN_HEIGHT // 2) - self.player.rect.centery

        # Update the position of all sprites by the offset
        for sprite in self.all_sprites:
            sprite.rect.x += player_offset_x
            sprite.rect.y += player_offset_y

        self.all_sprites.draw(self.screen)  # Draw all the sprites on the screen
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        # The main game loop
        while self.playing:
                        self.events()
                        self.update()
                        self.draw()
        self.running = False

    def game_over(self):
        # Handle the game over state
        pass

    def intro_screen(self):
        intro_text = [
            "Welcome to the Game!",
            "Instructions:",
            "Use the arrow keys to move the player character.",
            "Avoid the blocks and tall grass.",
            "Reach the water to win the game.",
            "Press any key to start."
        ]

        self.screen.fill(BLACK)

        font = pygame.font.Font(None, 36)

        for i, line in enumerate(intro_text):
            text = font.render(line, True, WHITE)
            text_rect = text.get_rect(center=(WIN_WIDTH // 2, (WIN_HEIGHT // 2) + (i * 40)))
            self.screen.blit(text, text_rect)

        pygame.display.flip()

        # Wait for a key press to continue
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    waiting = False


g = Game()
g.intro_screen()  # Show the intro screen
g.new()  # Start a new game
while g.running:
    g.main()  # Run the main game loop
    g.game_over()  # Handle the game over state

pygame.quit()
sys.exit()
