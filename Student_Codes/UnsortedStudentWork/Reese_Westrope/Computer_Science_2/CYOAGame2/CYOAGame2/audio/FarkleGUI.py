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

dice_images = []
dice_rolling_images = []

# since there are 6 dice images
for num in range(1, 7):
    dice_image = pygame.image.load('graphics/dice/' + str(num) + '.png')
    dice_images.append(dice_image)

# since there are 8 rolling dice images
for num in range(1, 9):
    dice_rolling_image = pygame.image.load('graphics/animation/roll' + str(num) + '.png')
    dice_rolling_images.append(dice_rolling_image)

rolling_aud = pygame.mixer.Sound('audio/roll_aud.mp3')
rolling_stop_aud = pygame.mixer.Sound('audio/roll_stop_aud.mp3')

is_rolling = False
rolling_images_counter = 0
dice_num_image = dice_images[0]
first = True

#game logic classes
class Dice:
    def __init__(self, x, y):
        self.faces = [1, 2, 3, 4, 5, 6]
        self.is_rolling = False
        self.rolling_images_counter = 0
        self.dice_image = dice_images[random.randint(0, 5)]
        self.x = x
        self.y = y

    def roll(self):
        result = random.choice(self.faces)
        return result

    def roll_animation(self, screen):
        if self.is_rolling:
            # showing rolling animation images
            screen.blit(dice_rolling_images[self.rolling_images_counter], (self.x, self.y))
            self.rolling_images_counter += 1
            if self.rolling_images_counter >= 8:
                self.is_rolling = False
                self.rolling_images_counter = 0
        else:
            screen.blit(dice_num_image, (self.x, self.y))



while True:

    die1 = Dice(20, 150)
    die2 = Dice(250, 150)
    die3 = Dice(450, 150)

    dice_list = [die1, die2, die3]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background_image, (0, 0))
    screen.blit(roll_message, (50, 300))



    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and is_rolling is False:
        is_rolling = True
        rolling_aud.play()
        # Roll each die separately and store the results in separate variables
        '''rand_num1 = die1.roll()
        rand_num2 = die2.roll()
        rand_num3 = die3.roll()
        # Use the random numbers to select the appropriate dice image for each die
        dice_num_image1 = dice_images[rand_num1 - 1]
        dice_num_image2 = dice_images[rand_num2 - 1]
        dice_num_image3 = dice_images[rand_num3 - 1]'''
        screen.blit(dice_rolling_images[rolling_images_counter], (250, 150))
        rolling_images_counter += 1
        first = True

        # start rolling and calculate dice num
    else:
        if is_rolling:
            # showing rolling animation images
            screen.blit(dice_rolling_images[rolling_images_counter], (250, 150))
            rolling_images_counter += 1
            if rolling_images_counter >= 8:
                is_rolling = False
                rolling_images_counter = 0
                # Roll each die separately and store the results in separate variables
                rand_num1 = die1.roll()
                rand_num2 = die2.roll()
                rand_num3 = die3.roll()
                # Use the random numbers to select the appropriate dice image for each die
                '''dice_num_image1 = dice_images[rand_num1 - 1]
                dice_num_image2 = dice_images[rand_num2 - 1]
                screen.blit(die1.dice_image, (400, 150))'''
                dice_num_image1 = die1.dice_image
                dice_num_image2 = die2.dice_image
                dice_num_image3 = die3.dice_image


        else:
            #screen.blit(dice_num_image1, (200, 150))
            #screen.blit(dice_num_image2, (300, 150))
            #screen.blit(dice_num_image3, (400, 150))
            screen.blit(die1.dice_image, (100, 150))
            screen.blit(die2.dice_image, (250, 150))
            screen.blit(die3.dice_image, (400, 150))
            if first:
                rolling_stop_aud.play()
                first = False



    '''key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and is_rolling is False:
        for dice in dice_list:
            if not dice.is_rolling:
                dice.is_rolling = True
                rolling_aud.play()
                rand_num_1 = random.randint(0, 5)
                rand_num_2 = random.randint(0, 5)
                rand_num_3 = random.randint(0, 5)
                dice_num_image_1 = dice_images[rand_num_1]
                dice_num_image_2 = dice_images[rand_num_2]
                dice_num_image_3 = dice_images[rand_num_3]
                dice.first = True

    for dice in dice_list:
        dice.roll_animation(screen)

        if dice.is_rolling and dice.rolling_images_counter == 0:
            rand_num_1 = die1.roll()
            rand_num_2 = die2.roll()
            rand_num_3 = die3.roll()
            dice_num_image_1 = dice_images[rand_num_1]
            dice_num_image_2 = dice_images[rand_num_2]
            dice_num_image_3 = dice_images[rand_num_3]

        else:
            screen.blit(dice_num_image_1, (200, 150))
            screen.blit(dice_num_image_2, (300, 150))
            screen.blit(dice_num_image_3, (400, 150))
            if first:
                rolling_stop_aud.play()
                first = False'''

        # start rolling and calculate dice num
    '''else:
        if is_rolling:
            # showing rolling animation images
            screen.blit(dice_rolling_images[rolling_images_counter], (250, 150))
            rolling_images_counter += 1
            if rolling_images_counter >= 8:
                is_rolling = False
                rolling_images_counter = 0

        else:
            screen.blit(dice_num_image, (250, 150))
            if first:
                rolling_stop_aud.play()
                first = False
            # show the dice which contains a number'''

    pygame.display.update()
    clock.tick(13)