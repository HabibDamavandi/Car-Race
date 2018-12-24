import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("lose.wav")
pygame.mixer.music.load("world.ogg")


display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)


gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Race Car')

clock = pygame.time.Clock()

carImg = pygame.image.load("Bug.png")

car_width = 48


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()   
            
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    TextSurf,TextRect = text_objects(msg,smallText)
    TextRect.center = ((x+(w/2)),(y + (h/2)))
    gameDisplay.blit(TextSurf,TextRect)  

def quitgame():
    pygame.quit()
    quit()

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',90)
        TextSurf, TextRect = text_objects("Let's Play Game",largeText)
        TextRect.center = ((display_width/2),(display_height/2 - 50))
        gameDisplay.blit(TextSurf,TextRect)
        button("Play!!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()


def GameScore(count):
    font = pygame.font.SysFont(None , 25)
    text = font.render("Score : "+str(count) , True , red)
    gameDisplay.blit(text,(10,10))


def stuff(stuffx,stuffy,stuffw,stuffh,color):
    pygame.draw.rect(gameDisplay,color,[stuffx,stuffy,stuffw,stuffh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text, True , black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

    time.sleep(2)
    game_loop()

def crash ():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf, TextRect = text_objects("You Crashed",largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Try agian",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)        

        pygame.display.update()


def game_loop():  

    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.8)   

    x_change = 0

    stuff_startx = random.randrange(0,display_width)
    stuff_starty = -700
    stuff_speed = 7
    stuff_width = 100
    stuff_height = 100

    Score = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -14
                elif event.key == pygame.K_RIGHT:
                    x_change = 14  
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0          


        x += x_change
        
        gameDisplay.fill(white)

        stuff(stuff_startx,stuff_starty,stuff_width,stuff_height,red)
        stuff_starty += stuff_speed

        GameScore(Score)

        car(x,y)        

        if x > display_width - car_width or x < 0:
            crash()

        if stuff_starty > display_height:
            stuff_starty = 0 - stuff_height
            stuff_startx = random.randrange(0,display_width)   
            Score += 1
            stuff_speed += 1
            

        if y < stuff_starty + stuff_height:
            if x > stuff_startx and x < stuff_startx + stuff_width or x + car_width > stuff_startx and x + car_width < stuff_startx + stuff_width:
                crash()    


        pygame.display.update()
        clock.tick(60)
        
game_intro()
game_loop()
pygame.quit()
quit()
