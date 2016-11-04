import random
import pygame
import cv2
import numpy as np

pygame.init()
size = [400, 400]
screen = pygame.display.set_mode(size)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def create_cat():
    # ears
    randear= random.randrange(-10,30,1)
    pygame.draw.polygon(screen,BLACK, [[65,10+randear],[65,45],[85,40]], 3)
    pygame.draw.polygon(screen,BLACK, [[135,10+randear],[135,45],[115,40]], 3)
    #face
    pygame.draw.circle(screen, BLACK, (100,100), 65,3)

    #eye
    randeye= random.randrange(-10,10,1)
    pygame.draw.circle(screen,BLACK, (75+randeye,90),10+randeye,10+randeye)
    pygame.draw.circle(screen,BLACK, (125+randeye,90),10+randeye,10+randeye)

    #whiskers
    randwhisk= random.randrange(-20,20,1)
    pygame.draw.line(screen,BLACK,[125,110],[180+randwhisk,80],3)
    pygame.draw.line(screen,BLACK,[125,120],[180+randwhisk,120],3)
    pygame.draw.line(screen,BLACK,[125,130],[180+randwhisk,160],3)
    pygame.draw.line(screen,BLACK,[75,110],[25-randwhisk,80],3)
    pygame.draw.line(screen,BLACK,[75,120],[25-randwhisk,120],3)
    pygame.draw.line(screen,BLACK,[75,130],[25-randwhisk,160],3)

    #mouth
    randmouth= random.randrange(1,17,1)
    pygame.draw.ellipse(screen,BLACK,[80,120,45,20+randmouth],3)
    

def create_dog():
    pygame.draw.circle(screen, BLACK, (100,100), 65,3)
    #eye
    randeye= random.randrange(-10,10,1)
    pygame.draw.circle(screen,BLACK, (75+ randeye,90),10+randeye,10+randeye)
    pygame.draw.circle(screen,BLACK, (125+randeye,90),10+randeye,10+randeye)

    #whiskers
    randwhisk= random.randrange(0,20,1)
    pygame.draw.line(screen,BLACK,[110,110],[140+randwhisk,100],3)
    pygame.draw.line(screen,BLACK,[110,120],[140+randwhisk,120],3)
    pygame.draw.line(screen,BLACK,[110,130],[140+randwhisk,140],3)
    pygame.draw.line(screen,BLACK,[85,110],[60-randwhisk,100],3)
    pygame.draw.line(screen,BLACK,[85,120],[60-randwhisk,120],3)
    pygame.draw.line(screen,BLACK,[85,130],[60-randwhisk,140],3)
    #nose
    randnose= random.randrange(-4,15,1)
    pygame.draw.ellipse(screen,BLACK,[85,100,30,55],3)
    pygame.draw.circle(screen,BLACK, (100,140),10+randnose,10+randnose)
    # ears
    randear= random.randrange(-10,30,1)
    pygame.draw.rect(screen,BLACK,[160,90,25,30+randear],3)


class Cats_Dogs:

    def draw_frame(self):
        screen.fill(WHITE)
        pick_animal = random.choice([1,2])
        if pick_animal ==1:
            self.animal= 'cat'
            create_cat()
        if pick_animal== 2:
            self.animal= 'dog'
            create_dog()

        x_t1= pygame.surfarray.pixels3d(screen)
        x_t4= cv2.cvtColor(cv2.resize(x_t1, (80, 80)), cv2.COLOR_BGR2GRAY)
        ret, x_t4 = cv2.threshold(x_t4,1,255,cv2.THRESH_BINARY)                    
        state = np.stack((x_t4,x_t4), axis =2)
        return pick_animal, state
            
        
#debug code
##draw = Cats_Dogs()
##print draw.draw_frame()
##pygame.quit()
##        
        
