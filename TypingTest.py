import pygame
from pygame.locals import *
import sys
import time
import random

#checks for wpm
def wpm(source, time):
    words = len(source.split())
    per_second = words / time
    return per_second*60

#checks for accuracy
def accuracy(input,source):
    length_source = len(source)
    if len(source) > len(input):
        length = len(input)
    else:
        length = len(source)
    matches = 0
    for i in range(0, length):
        if input[i] == source[i]:
            matches = matches + 1
    return matches / length_source * 100

#draws text to the screen
def drawText(screen, text, x, y,fontSize, colour):
    font = pygame.font.SysFont("arial", fontSize)
    renderedText = font.render(text, 1, colour)
    textBox = renderedText.get_rect(center=(x, y))
    screen.blit(renderedText, textBox)

#the list of sentences that could be randomply selected
sentences = ["Hello there, General Kenobi.", "He hated that he loved what she hated about hate.",
             "Flash photography is best used in full sunlight.",
             "The rain pelted the windshield as the darkness engulfed us.",
             "He decided water-skiing on a frozen lake wasn’t a good idea.",
             "He swore he just saw his sushi move.",
             "The tortoise wants to be a sea turtle.",
             "It doesn't sound like that will ever be on my travel list."
             ]
#initialize the game
pygame.init()
screen = pygame.display.set_mode((750,500))
pygame.display.set_caption('Typing Test')
#loop the game
while True:
    #fill screen and count down timer
    screen.fill((176, 216, 230))
    drawText(screen, "3", 750/2, 500/2, 150, (0, 0, 0))
    pygame.display.update()
    time.sleep(1)
    screen.fill((176, 216, 230))
    drawText(screen, "2", 750/2, 500/2, 150, (0, 0, 0))
    pygame.display.update()
    time.sleep(1)
    screen.fill((176, 216, 230))
    drawText(screen, "1", 750/2, 500/2, 150, (0, 0, 0))
    pygame.display.update()
    time.sleep(1)
    screen.fill((176, 216, 230))
    drawText(screen, "Go", 750/2, 500/2, 150, (0, 0, 0))
    pygame.display.update()
    time.sleep(0.15)
    
    #default variables for each round
    sentence = random.choice(sentences)
    playing = True
    roundOver = False
    firstStroke = True
    userInput = ''
    start = 0
    end = 0
    total = 0
    
    #loop each round
    while(playing):
        screen.fill((176, 216, 230))
        pygame.draw.rect(screen, (255,255,255), (50, 250, 650, 50), 2)
        pygame.draw.rect(screen, (0,0,0), (50, 250, 650, 50))
        pygame.draw.rect(screen, (0, 0, 0), (550, 350,100, 100))
        drawText(screen, "Typing Test", 750/2, 65, 100, (0,0,0,))
        drawText(screen, "Reset", 600, 400, 40, (255,255,255))
        drawText(screen, sentence, 750 / 2, 200, 30, (0, 0, 0,))
        drawText(screen, userInput, 750/2, 274, 26, (250, 250, 250))
        #print results if round is over
        if roundOver is True:
            drawText(screen, "Time is: " + str(round(total,2)) + " secs", 175, 340, 40, (0,0,0,))
            drawText(screen, "Accuracy is: " + str(round(accuracy(userInput,sentence),2)) + "%", 175, 390, 40, (0, 0, 0,))
            drawText(screen, "WPM is: " + str(round(wpm(sentence,total))),175, 440, 40, (0, 0, 0,))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                #reset button
                if (x >= 550 and x <= 650 and y >= 350 and y <= 450):
                    playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    end = time.time()
                    total = end - start
                    roundOver = True
                elif event.key == pygame.K_BACKSPACE:
                    userInput = userInput[:-1]
                else:
                    if firstStroke is True:
                        start = time.time()
                        firstStroke = False
                    userInput += event.unicode
