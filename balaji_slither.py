
###Make sure to have pygame on your computer
######
##Sanath Balaji - Slither(Snake game) 2018.
##This game makes use to the PyGame package in Python and uses the Arrow keys to control the snake.
##C to play, P to pause nand q to quit
##This version of the snake game was modified from the tutorial posted by Syntec (on behalf of TheNewBoston.com)
##All modifications and changes I made are commented in-line below.
######








import pygame
import time
import random

pygame.init()

# Defines Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (66, 89, 244)
orange = (244, 133, 65)


# Width of the window
display_width = 800
display_height = 600

# Display of the GUI
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('SLITHER')

icon = pygame.image.load('download.jpg')
pygame.display.set_icon(icon)

backgroundimg=pygame.image.load('durant.jpg')
img = pygame.image.load('snake.png')
appleimg= pygame.image.load('apple.png')
preyimg= pygame.image.load('durant.jpg')


'''
gameExit = False

lead_x = display_width / 2
lead_y = display_height / 2

lead_x_change = 0
lead_y_change = 0
'''

clock = pygame.time.Clock()

PreyThickness = 30
AppleThickness = 30
block_size = 20
FPS = 15

direction = "right"

small = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


def pause():

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        gameDisplay.blit(backgroundimg,[0,0])

        message_to_screen("Game has been paused",
                          black,
                          -100,
                          size = "large")

        message_to_screen("Press C to continue or Q to quit.",
                          black,
                          25)
        pygame.display.update()
        clock.tick(5)

def score(score):
    text = small.render("Score: "+str(score), True, blue)
    gameDisplay.blit(text, [0,0])

def time(time):
    text = small.render("Time: "+str(time),True,orange)
    gameDisplay.blit(text,[0,50])

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - AppleThickness))  # /10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - AppleThickness))  # /10.0)*10.0

    return randAppleY,randAppleY


def randPreyGen():
    randPreyX = round(random.randrange(0, display_width - PreyThickness))  # /10.0)*10.0
    randPreyY = round(random.randrange(0, display_height - PreyThickness))  # /10.0)*10.0

    return randPreyX,randPreyY






def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        # 
        message_to_screen("Welcome to Slither", red, -100, size='large')
        message_to_screen('The objective of this game is to eat dem apples to keep doctors away.',
                          white,
                          10)
        message_to_screen('The more you eat, the LONGER you become. So watch out.',
                          white,
                          50)
        message_to_screen('Press C to play, P to pause, or Q to quit',
                           blue,
                          180)

        pygame.display.update()
        clock.tick(15)


def snake(block_size, snakeList):

    if direction == "right":
        head = pygame.transform.rotate(img,270)
    if direction == "left":
        head = pygame.transform.rotate(img,90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img,180)

    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, red, [XnY[0], XnY[1], block_size, block_size])


def text_objects(text, color, size):
    if size == "small":
        textSurface = small.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


# Defeat message
def message_to_screen(msg, color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2)+ y_displace
    gameDisplay.blit(textSurf, textRect)


# Defines moving speeds
def gameLoop():
    global direction

    direction = 'right'
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen()

    randPreyX, randPreyY = randPreyGen()

    gameTime=0

    while not gameExit:
        gameTime +=1

        while gameOver == True:
            gameDisplay.fill(black)
            message_to_screen('Your snake has died', red, -50, size = "large")
            message_to_screen('Press C to play again or Q to quit', red, 50, size= "medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Keys for control
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0

                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()
            # If out of bounds, game over
            if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
                gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        # Color of game display
        gameDisplay.fill(white)


        # Draws apple
        AppleThickness = 30
        PreyThickness = 40
        #pygame.draw.rect(gameDisplay, green, [randAppleX, randAppleY, AppleThickness, AppleThickness])


        gameDisplay.blit(appleimg,(randAppleX,randAppleY))
        gameDisplay.blit(preyimg, (randPreyX, randPreyY))
        

        # Draws snake
        #pygame.draw.rect(gameDisplay, red, [lead_x, lead_y, block_size, block_size])

        # Defines variables for the snake
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        # Makes it so when moving, the snake will be the same size unless eating apple.
        if len(snakeList) > snakeLength:
            del snakeList[0]

        # When Collisions occur, game over
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)

        score(snakeLength-1)

        time(gameTime)

        pygame.display.update()

        # If the snake crosses boundary of the apple
        # When snake eats apple, increase snake Length by 1
        speed= 0
        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            print('x')
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                # If the snake crosses boundary of the apple
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
                speed += 0.5



            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

        if lead_x > randPreyX and lead_x < randPreyX + PreyThickness or lead_x + block_size > randPreyX and lead_x + block_size < randPreyX + PreyThickness:
            print('x')
            if lead_y > randPreyY and lead_y < randPreyY + PreyThickness:
                # If the snake crosses boundary of the apple
                randPreyX, randPreyY = randPreyGen()
                snakeLength += 2
                speed += 1



            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 2

        clock.tick(FPS+speed)

    pygame.quit()
    quit()

game_intro()
gameLoop()
