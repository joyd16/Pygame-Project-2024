# Pygame Project 
# Author: Joy Dong
# May 28, 2024

import pygame as pg

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 1000  # Pixels
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)

# class Player(pg.sprite.Sprite):
#     # def __init__ (self):
#     #     super().__init__()
        
#     #     self.image = a
#     #     self.rect = a

#     # def update(self):


def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    background_x = 0

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    pg.display.set_caption("<WINDOW TITLE HERE>")


    # Load the image
    bg_image = pg.image.load("./Images/background_one.png")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        background_x -= 3
        
        # --- Update the world state

        # --- Draw items
        screen.blit(bg_image, (background_x, 0))
        if bg_image == (WIDTH, 0):
            screen.blit(bg_image, (background_x, 0))
        

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps

    pg.quit()


def main():
    start()


if __name__ == "__main__":
    main()