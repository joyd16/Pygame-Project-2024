# Pygame Project 
# Author: Joy Dong
# May 28, 2024

import pygame as pg
import random

# Amount of books 
NUM_BOOKS: 10

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 900  # Pixels
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/Batman.webp")
        self.rect = self.image.get_rect()

        self.lives = 3

    def update(self):

        # Update the location
        # Controlled by the mouse
        self.rect.centerx = pg.mouse.get_pos() [0]
        self.rect.centery = pg.mouse.get_pos() [1]

class Book(pg.sprite.Sprite):
    def __init__(self, size: int):
        super().__init__()

        # Book appearance
        self.image = pg.Surface((size, size))
        pg.draw.circle(self.image, WHITE, (size // 2, size //2),  size // 2)
        
        self.rect = self.image.get_rect()

        # Spawn book at the top of the screen

        self.rect.x = random.randrange(0, WIDTH)
        self.rect.y = random.randrange(0, HEIGHT)

        self.vel_y = -4

    def update(self):
        self.rect.y -= self.vel_y

        # If it falls off the screen, teleport back to the top of the screen

        if self.rect.bottom >= HEIGHT + 10:
            self.rect.y = -10
            self.rect.x = self.rect.x

        # And lose a life


def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()
    book_sprites = pg.sprite.Group()

    player = Player()
    all_sprites.add(player)

    for _ in range(NUM_BOOKS):
        book = Book()
        all_sprites.add(book)
        book_sprites.add(book)

    pg.display.set_caption("<WINDOW TITLE HERE>")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state

        all_sprites.update()


        # 
        if len(book_sprites) <= 9:
            for _ in range(NUM_BOOKS):
                book = Book()
                all_sprites.add(book)
                book_sprites.add(book)

        # Increase speed 

                # for book in book_sprites:
                #     sprite.increase_speed()

        book_collided = pg.sprite.spritecollide(player, book_sprites, False)

        for book in book_collided:
            player.lives -= 0.1 
            print(int(player.lives))



        # --- Draw items
        screen.fill(BLACK)

        # Draw all of the sprites
        
        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps

    pg.quit()


def main():
    start()


if __name__ == "__main__":
    main()