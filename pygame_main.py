# Pygame Project 
# Author: Joy Dong
# May 28, 2024

# Used "Pixeled" font by OmegaPC777 on Dafont.com

import pygame as pg
import random

# Make the book smaller
BOOK_IMAGE = pg.image.load("./images_coding/book.png")
BOOK_IMAGE_SMALL = pg.transform.scale(BOOK_IMAGE, (BOOK_IMAGE.get_width() // 1.7, BOOK_IMAGE.get_height() // 1.7))

# Make Day larger
DAY_IMAGE = pg.image.load("./images_coding/day.png")
DAY_IMAGE_LARGE = pg.transform.scale(DAY_IMAGE, (DAY_IMAGE.get_width() * 1.5, DAY_IMAGE.get_height() * 1.5))


# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

TEXT_ORANGE = (237, 112, 55)
TEXT_CREAM = (250, 245, 225)

WIDTH = 900  # Pixels
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = DAY_IMAGE_LARGE
        self.rect = self.image.get_rect()

        self.image = pg.transform.scale(self.image, (self.image.get_width() // 4, self.image.get_height() // 4))
        self.rect = self.image.get_rect()

        self.lives = 3

        # Starting speed
        self.change_x = 0

    def update(self):

        # Keep at the bottom of the screen
        if self.rect.top < HEIGHT - 210:
            self.rect.top = HEIGHT - 210

        # Keep within the screen
        if self.rect.left < 0:
            self.rect.left = 0
            
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        # Movements 
        self.rect.x += self.change_x
    

    def left(self):
        # Left arrow to go left
        self.change_x = -12

    def right(self):
        # Right arrow to go right
        self.change_x = 12

    def stop(self):
        # Stop moving when nothing is pressed
        self.change_x = 0

class Book(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Book appearance
        self.image = BOOK_IMAGE_SMALL
        self.rect = self.image.get_rect()
        
        self.rect = self.image.get_rect()

        # Spawn book at the top of the screen
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = HEIGHT

        # Speed
        self.vel_y = 6

    def update(self):
        # Movement
        self.rect.y += self.vel_y

        if self.rect.bottom >= HEIGHT + 10:
            self.rect.y = -10

        # Kill if it hits the floor
        if self.rect.bottom < 0:
            self.kill()

class Ground(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
    
        self.image = pg.image.load("./images_coding/ground.webp")
        self.rect = self.image.get_rect()

        # Set location of the floor 
        
        self.rect.bottom = HEIGHT
        

def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # Hide the mouse
    pg.mouse.set_visible(False)

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # 1) From George's Jungle Jam
    # Falling time
    book_fallen = 1500
    last_book_fallen = pg.time.get_ticks()

    # 2) From George's Jungle Jam
    # Difficulty
    difficulty = 0

    # Score
    score = 0

    # Font
    font = pg.font.Font("Pixeled.ttf", 15)

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    # Book sprites go in this sprite Group
    book_sprites = pg.sprite.Group()


    ground = Ground()
    all_sprites.add(ground)

    player = Player()
    all_sprites.add(player)


    pg.display.set_caption("<WINDOW TITLE HERE>")

    bg_image = pg.image.load("./images_coding/background.png")


    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

            # Player movements 
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    player.right()
                if event.key == pg.K_LEFT:
                    player.left()                
            if event.type == pg.KEYUP:
                player.stop()

        # --- Update the world state

        all_sprites.update()

        # Keep track of the books collected
        books_collided = pg.sprite.spritecollide(player, book_sprites, True)

        # For every book collected
        for book in books_collided:
            # Increase the score by 1
            score += 1
            # Print the score
            print(f"Score: {score}")

        # 3) From George's Jungle Jam
        # After cooldown for book falling
        if pg.time.get_ticks() > last_book_fallen + book_fallen:
            # Reset cooldown
            last_book_fallen = pg.time.get_ticks()
            book = Book()
            all_sprites.add(book)
            book_sprites.add(book)

        # 4) From George's Jungle Jam
        # Increase speed as difficulty increases
        if score  >= difficulty:
            book_fallen-= 200
            difficulty += 10

        # When a book hits the ground
        book_on_ground = pg.sprite.spritecollide(ground, book_sprites, True)

            # make it not disappear and stop losing lives

        # For every book that hits the ground
        for book in book_on_ground:
            # Lose one life
            player.lives -= 1
            print(int(player.lives))

        # If lives are all gone, end the game
        if player.lives == 0:
            quit()
            # Add "Play Again" later

        # --- Draw items
        screen.fill(BLACK)

        screen.blit(bg_image, (0,0))

        # Score and lives counter
        score_image = font.render(f"SCORE: {score}", True, TEXT_ORANGE)
        lives_image = font.render(f"LIVES: {int(player.lives)}", True, TEXT_CREAM)
        #Blit the surface on the screen
        screen.blit(score_image, (5, 0))
        screen.blit(lives_image, (5, 35))

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