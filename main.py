# main.py
import pygame
from map.block import *
from utils.config import *
from map.ground import *
from map.dirtpath import DirtPath
from characters.player import *
from utils.spritesheets import *
from map.tallgrass import *
from map.tilemap import *
import sys



class Inventory:
    def __init__(self):
        self.items = [[None]*5 for _ in range(5)] # 5x5 inventory slots
        
    def add_item(self, item):
        for i in range (5):
            for j in range (5):
                if self.items[i][j] is None:
                    self.items[i][j] = item
                    return True
        return False
    
    def remove_item(self, item):
        for i in range (5):
            for j in range (5):
                if self.items[i][j] == item:
                    self.items[i][j] = None
                    return True
        return False # Item Not Found
    
    
    def has_item(self, item):
        for i in range (5):
            for j in range (5):
                if self.items[i][j] == item:
                    return True
        return False
            
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Load in Spritesheets
        self.character_spritesheet = Spritesheets('img/character.png')  # Load the spritesheet for the character
        self.terrain_spritesheet = Spritesheets('img/terrain.png')  # Load the spritesheet for the terrain
        
        self.player = None  # Reference to the player instance
        
        self.inventory = Inventory()
        self.show_inventory = False
        
        
    def drawInventory(self):
        if self.show_inventory:
            slot_width = 40
            slot_height = 40
            padding = 5
            for i in range (5):
                for j in range (5):
                    rect = pygame.Rect(WIN_WIDTH - (5-j)*(slot_width+padding), WIN_HEIGHT - (5-i)*(slot_height+padding), slot_width, slot_height)
                    pygame.draw.rect(self.screen, WHITE, rect, 2)
                    if self.inventory.items[i][j] is not None:
                        # Draw Item In Slot (replace 'item_image' with your items image)
                        self.screen.blit(item_image, rect)
                        
        
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    self.show_inventory = not self.show_inventory
                
        
            
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
        self.drawInventory()
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
