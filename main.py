import pygame as pg, random

from classes.player import Player
from classes.monster import Monster
from classes.game import Game

# Initialize the game
pg.init()

# Set display window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Monster Wrangler")

# Set frame rate
FPS = 60
clock = pg.time.Clock()


# Create a player group and Player object
player_group = pg.sprite.Group()
player = Player(WINDOW_WIDTH, WINDOW_HEIGHT)
player_group.add(player)

# Create a monster group
monster_group = pg.sprite.Group()

# main game loop
running = True

# Create a game object
my_game = Game(
    player, monster_group, WINDOW_WIDTH, WINDOW_HEIGHT, FPS, display_surface, running
)
my_game.pause_game("Monster Wrangler", "Press 'Enter' to begin")
my_game.start_new_round()

while running:
    # Check for events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Fill the display
    display_surface.fill((0, 0, 0))

    # Draw the player
    player_group.update()
    player_group.draw(display_surface)

    # Draw the monsters
    monster_group.update()
    monster_group.draw(display_surface)

    # Update and draw the game
    my_game.update()
    my_game.draw()

    # Update the display
    pg.display.update()
    clock.tick(FPS)

# Quit the game
pg.quit()
