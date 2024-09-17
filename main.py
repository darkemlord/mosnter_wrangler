import pygame as pg, random

from classes.player import Player

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


# Create a player
player_group = pg.sprite.Group()
player = Player(WINDOW_WIDTH, WINDOW_HEIGHT)
player_group.add(player)

# main game loop
running = True
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

    # Update the display
    pg.display.update()
    clock.tick(FPS)

# Quit the game
pg.quit()
