print('Hello World')
#importing the os module
import os

#to get the current working directory
directory = os.getcwd()

print(directory)

os.listdir(directory) # returns list

# Get the list of all files and directories
path = "C:/Users/Carlie/SwosuCsPythonExamples/CYOAG/Simple_Game"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)

print('Hello World #2')
#Add Image to game
#pip install pygame
import pygame
from pygame.locals import *

pygame.init()

# define the RGB value
# for white colour
white = (255, 255, 255)
# assigning values to X and Y variable
X = 400
Y = 400

# create the display surface object
# of specific dimension..e(X, Y).
screen = pygame.display.set_mode((X, Y ))

# set the pygame window name
pygame.display.set_caption('Carlie Image')

#screen = pygame.display.set_mode((500,500),0,32)

defeat = pygame.image.load('DEFEAT.jpg')
#victory = pygame.image.load(r'C:\Users\Carlie\SwosuCsPythonExamples\CYOAG\Simple_Game\VICTORY.jpg')
victory = pygame.image.load(r'C:/Users/Carlie/SwosuCsPythonExamples/CYOAG/Simple_Game/VICTORY.jpg')
#image = pygame.image.load(r'C:\Users\user\Pictures\geek.jpg')

# infinite loop
while True :
  
    # completely fill the surface object
    # with white colour
    screen.fill(white)
  
    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    screen.blit(victory, (0, 0))
  
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get() :
  
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT :
  
            # deactivates the pygame library
            pygame.quit()
  
            # quit the program.
            quit()
  
        # Draws the surface object to the screen.  
        pygame.display.update() 

'''while True:
    screen.blit(defeat,(0,0))

    pygame.display.update()'''