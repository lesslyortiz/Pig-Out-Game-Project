import pygame
import time 
import random
import math
from replit import audio

#initializers: 
screen     = pygame.display.set_mode((800, 700)) #window 900 x 700 pixels
pygame.init # Initializes pygame 
pygame.display.init # Initializes the display
background = pygame.image.load('background.png')
background2= pygame.image.load('Main-menu.png')
Gameoverscreen = pygame.image.load('Game-over-screen.png')
clock      = pygame.time.Clock()
running    = True #keeps our while loop below going 
menu       = True


#background_music ##Still needs some work
source = audio.play_file('Pig-Out-Opening.mp3')
volume = 2
loops  = -1


#font initializer
pygame.font.init()
score     = 0
scorefont = pygame.font.Font('freesansbold.ttf', 32)
scorex    = 70
scorey    = 655


#chicken's sprite code:
chickenpic     = pygame.image.load('chicken.png') #his image
chickenpicx    = 500 #his initial x coordinate 
chickenpicy    = 350 #his initial y coordinate 
chickenchangex = 0 #change in his x coordinate (will change in our while loop if the user moves him)
chickenchangey = 0 #change in chicken's y coordinate (^^^)


def Pig(x, y):
    """This is chicken's movement function that draws, or 'blits', chicken to the screen to whatever (x, y) coordinate is given as the parameter)
    """ 
    screen.blit(chickenpic, (chickenpicx, chickenpicy)) 


#the food's (cilantro) sprites' code:
cilantropic  = []
cilantropicx = []
cilantropicy = []
numcilantro  = 5

for i in range(numcilantro): #appends 5 items to each of the 3 lists made above of png cilantro images,random initial x and y coordiante lists
    cilantropic.append(pygame.image.load('cilantro.png'))
    cilantropicx.append(random.randint(150, 700))
    cilantropicy.append(random.randint(150, 600))


def Cilantro(cilantropicx, cilantropicy , i): 
    """This function draws one of the cilantro images from the list of cilantro images we created, cilantropic, and this is done by using the index value paramter in this function and draws this images to the x y coordinate parameter given for (cilantropicx, cilantropicy),  """
    screen.blit(cilantropic[i], (cilantropicx, cilantropicy))



def Collision(cilantropicx, cilantropicy, chickenpicx, chickenpicy):
    """This function calculates the distance between chicken and a cilantro image on the screen to check if they "collided" and returns True or False. Since our images appear to accurately "collide" when their distance is 40 pixels, the function returns True at this occurence. This is done by using both chicken's x y coordinate variables and the cilantro's x y coordiante variables as parameters to use in the distance equation""" 
    dist = math.sqrt((math.pow(chickenpicx - cilantropicx, 2)) + (math.pow(chickenpicy - cilantropicy, 2))) 
    if dist <= 40: # because taking into account how thick in pixels chicken and food are
        audio.play_file('Eating-Sound.mp3')
        return True
    else:
        return False



def Score(scorex, scorey): 
    """This function displays the score fraction to the screen with the x,y coordinates of where this is displayed on the screen as the parameters. This function aslo initializes the printedscore variable that sets the font, color, and takes in & casts our score variable's value to a string so that our score may be displayed properly"""
    printedscore = scorefont.render(str(score) + "/ 10 Cilantros", True, (8,96,168))
    screen.blit(printedscore, (scorex, scorey))


#this is our while loop that created the starting screen image and allows the user to click on the screen to start the game
while menu:
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          menu = False
    screen.fill((0, 0, 0))      
    clock.tick(30)
    screen.blit(background2, (0,0))
    pygame.display.update()


#the following while loop contains actions that we want to keep going continuously as the game goes on:
 ##main menu code ##still needs work and background image
while running == True:

    screen.fill((0, 0, 0)) #makes the window black 
    screen.blit(background, (0,0)) #draws our background to the window
    
    
    #updates chicken's NEW coordinates based off user input with every loop iteration:
    chickenpicx = chickenpicx + chickenchangex 
    chickenpicy = chickenpicy + chickenchangey
    Pig(chickenpicx, chickenpicy) #calls chicken to appear with current coordinates


    #this for loop checks if the user inputs stuff and if so how to change chicken's coordinates:
    for event in pygame.event.get(): #goes through 'events', as in the keys that are hit, that python keeps logs of in pygame.event.get()
        if event.type == pygame.KEYDOWN: #checks if the user pressed a key at all, if so, checks which one and increases or decreases chicken's x or y coordinates accordingly 
            if event.key == pygame.K_LEFT:
                chickenchangex = -5
            if event.key == pygame.K_RIGHT:
                chickenchangex = 5
            if event.key == pygame.K_UP:
                chickenchangey = -5
            if event.key == pygame.K_DOWN:
                chickenchangey = 5
                
        if event.type == pygame.KEYUP: #checks if the user stopped pressing a key so that chickens coordinates get "changed" by 0 instead of +/-6
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT):
                chickenchangex = 0
            if (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
                chickenchangey = 0
            
                         
    #boundaries for chicken to not fly off and out of the 800x700 border (makes sure he's "redrawn" back within the borders if he crosses them):
    if chickenpicx   <= 0: 
        chickenpicx   = 0 
    elif chickenpicx >= (800 -120): #taking into consideration chicken's 120 pixel width
        chickenpicx   = (800 - 120)

    if chickenpicy   <= 100:
        chickenpicy   = 100 
    elif chickenpicy >= (700 - 80): #taking into consideration chicken's 80 pixel height
        chickenpicy   = (700 - 80)
    #add thingies you also want to occur when they collide here

#####START ATTRIBUTED CODE SECTION HERE:
#code created with the help of Youtube --->>> https://www.youtube.com/watch?v=FfWpgLFMI7w&ab_channel=freeCodeCamp.org :
    #for each cilantro in the list cilantropic:
    for i in range(numcilantro):
        collision           = Collision(cilantropicx[i], cilantropicy[i], chickenpicx, chickenpicy) #we used indexing to iterate and use each of the corresponing random initial x y coordinate list made previously 
        if collision        == True: #if chicken eats the cilantro:
            score           = score + 1 #score update here
            cilantropicx[i] = random.randint(150, 700) #these randomize cilantro coordinates
            cilantropicy[i] = random.randint(150, 600)  
        Cilantro(cilantropicx[i], cilantropicy[i], i) # calls cilantro to be redisplayed
#####END ATTRIBUTED CODE SECTION HERE

    if score == 10: #quits game after 10 cilantros
        break 


    Pig(chickenpicx, chickenpicy) #these call to display chicken and the score with their current coordinates/score
    Score(scorex, scorey) 


    pygame.display.update() #re-draw all images with their updates to the window
   
#this draws the game over zcreen once the user wins the game
screen.blit(Gameoverscreen, (0,0)) 
pygame.display.update()
time.sleep(10000)
   
    
  
