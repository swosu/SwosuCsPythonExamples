import pygame
from sys import exit
import random

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Dice Roll Stimulator")

background_image = pygame.image.load('graphics/background2.png')
font = pygame.font.Font('font/SunnyspellsRegular.otf', 50)
roll_message = font.render("press SPACEBAR to start rolling", True, (255, 235, 193))


rolling_aud = pygame.mixer.Sound('audio/roll_aud.mp3')
rolling_stop_aud = pygame.mixer.Sound('audio/roll_stop_aud.mp3')

is_rolling = False
rolling_images_counter = 0
#dice_num_image = dice_images[0]
first = True


class Dice:
    def __init__(self, x, y):
        self.faces = [1, 2, 3, 4, 5, 6]
        self.is_rolling = False
        self.rolling_images_counter = 0
        self.dice_images = []
        self.dice_rolling_images = []
        self.load_dice_images()
        self.load_rolling_images()
        self.dice_num_image = self.dice_images[0]
        self.x = x
        self.y = y
        self.animate = True
        

    def roll(self):
        result = random.choice(self.faces)
        return result

    def load_dice_images(self):
        for num in range(1, 7):
            dice_image = pygame.image.load('graphics/dice/' + str(num) + '.png')
            self.dice_images.append(dice_image)

    def load_rolling_images(self):
        for num in range(1, 9):
            dice_rolling_image = pygame.image.load('graphics/animation/roll' + str(num) + '.png')
            self.dice_rolling_images.append(dice_rolling_image)

    def roll_animation(self, screen):
        global first
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.is_rolling is False:
            self.is_rolling = True
            rolling_aud.play()
            rand_num = random.randint(0, 5)
            self.dice_num_image = self.dice_images[rand_num]
            screen.blit(self.dice_rolling_images[self.rolling_images_counter], (self.x, self.y))
            self.rolling_images_counter += 1
            first = True

            # start rolling and calculate dice num
        else:
            if self.is_rolling:
                # showing rolling animation images
                screen.blit(self.dice_rolling_images[self.rolling_images_counter], (self.x, self.y))
                self.rolling_images_counter += 1
                if self.rolling_images_counter >= 8:
                    self.is_rolling = False
                    self.rolling_images_counter = 0

            else:
                screen.blit(self.dice_num_image, (self.x, self.y))
                if first:
                    rolling_stop_aud.play()
                    first = False
                # show the dice which contains a number




if __name__ == "__main__":

    die1 = Dice(20, 35)
    die2 = Dice(250, 35)
    die3 = Dice(450, 35)
    die4 = Dice(20, 170)
    die5 = Dice(250, 170)
    die6 = Dice(450, 170)

    dice_list = [die1, die2, die3, die4, die5, die6]


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            rolling_aud.play()
            for die in dice_list:
                die.is_rolling = True
                rand_num = random.randint(0, 5)
                die.dice_num_image = die.dice_images[rand_num]

        screen.blit(background_image, (0, 0))
        screen.blit(roll_message, (50, 300))

        for die in dice_list:
            die.roll_animation(screen)


        pygame.display.update()
        clock.tick(13)