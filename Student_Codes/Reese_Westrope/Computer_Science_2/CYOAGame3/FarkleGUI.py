import pygame
from sys import exit
import random

pygame.init()
clock = pygame.time.Clock()

screen_width = 500
screen_height = 700
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Dice Roll Simulator")

background_image = pygame.image.load('graphics/background2.png')
font = pygame.font.Font('font/SunnyspellsRegular.otf', 50)

player_name = font.render("Player:", True, (255, 235, 193))
player_score = font.render("Score:", True, (255, 235, 193))


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

class Button():

    def __init__(self, x, y, width, height, text='', color=(75, 38, 5), highlight_color=(103, 63, 30), function=None, param=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.highlight_color = highlight_color
        self.text = text
        self.function = function
        self.highlighted = False
        self.parameter = param
        
    def draw(self, surface):
        if self.highlighted:
            pygame.draw.rect(surface, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)
        
        font = pygame.font.Font('font/SunnyspellsRegular.otf', 50)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.function:
                    if self.parameter is not None:
                        self.function(self.parameter)
                    else:
                        self.function()
                
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.highlighted = True
            else:
                self.highlighted = False

'''def rolling_animation_space(dice_list):
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        rolling_aud.play()
        for die in dice_list:
            die.is_rolling = True
            die_roll_index = die.roll() - 1#random.randint(0, 5)
            die.dice_num_image = die.dice_images[die_roll_index]'''

def rolling_animation_button(dice_list):
    rolling_aud.play()
    for die in dice_list:
        die.is_rolling = True
        die_roll_index = die.roll() - 1#random.randint(0, 5)
        die.dice_num_image = die.dice_images[die_roll_index]

if __name__ == "__main__":


    

    die1 = Dice(70, 135)
    die2 = Dice(285, 135)
    die3 = Dice(500, 135)
    die4 = Dice(70, 270)
    die5 = Dice(285, 270)
    die6 = Dice(500, 270)

    dice_list = [die1, die2, die3, die4, die5, die6]

    roll_button_width = 120
    roll_button_height = 80
    roll_button_x = 150
    roll_button_y = 400
    roll_button = Button(roll_button_x, roll_button_y, roll_button_width, roll_button_height, text='Roll', function=rolling_animation_button, param=dice_list)

    pass_button_width = 120
    pass_button_height = 80
    pass_button_x = 400
    pass_button_y = 400
    pass_button = Button(pass_button_x, pass_button_y, pass_button_width, pass_button_height, text='Pass', function=lambda: print('pass button pressed'), param=None)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            else:
                roll_button.handle_event(event)
                pass_button.handle_event(event)

        screen.blit(background_image, (0, 0))
        screen.blit(player_name, (50, 50))
        screen.blit(player_score, (475, 50))

        for die in dice_list:
            die.roll_animation(screen)

        roll_button.draw(screen)
        pass_button.draw(screen)

        pygame.display.update()
        clock.tick(13)
