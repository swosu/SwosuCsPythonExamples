import pygame

from pygame.locals import *

pygame.init()

class Player:
    x = 10
    y = 10 
    speed = 1 

    def moveRight(self):
        self.x = self.x + self.speed 

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed
    
    def moveDown(self):
        self.y = self.y + self.speed

pygame.event.pump()
keys = pygame.key.get_pressed()



if (keys[K_RIGHT]):
    print ("Right arrow pressed.")

from pygame.locals import *
import pygame 

class Player:
    x = 10 
    y = 10
    speed = 1 

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed

class App:
    windowWidth = 800
    windowHeight = 600
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.player = Player()

    # set up pygame on init
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Pygame pythonspot.com example')

        self._running = True
        self._image_surf = pygame.image.load("pygame.png").convert()
    
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False 
    
    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.bill(self._image_surf,(self.player.x,self.player.y))

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False 

        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_presed()

            if (keys[K_RIGHT]):
                self.player.moveRight()

            if (keys[K_LEFT]):
                self.player.moveLeft()

            if (keys[K_UP]):
                self.player.moveUp()

            if (keys[K_DOWN]):
                self.player.moveDown()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()

