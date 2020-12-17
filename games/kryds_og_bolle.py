import numpy as np
import pygame
import time


class Game():
    games_played = 0
    points=[0,0]

    def __init__(self, size):
        self.gameOver=False
        self.size=size
        self.board=numpy.zeros((size, size), dtype=int)
        self.isPlayer1 = True

    def changePlayer(self):
        self.isPlayer1=not self.isPlayer1

    def endGame(self):
        self.gameOver=True
        Game.games_played+=1

    def makeMove(self, x, y):
        if self.isPlayer1:
            self.board[x][y]=1
        else:
            self.board[x][y]=2

pygame.init()
screen = pygame.display.set_mode((468, 400))
pygame.display.set_caption('Monkey Fever')
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

oldGames=[]
def playGame():
    currentGame=Game()
    while not currentGame.GameOver:






gamesToPlay=0
while gamesToPlay<1:
    try:
        gamesToPlay=input("How many games do you want to play? ")
    except:
        print("invalid input")


while Game.games_played!=gamesToPlay:
    playGame()


if pygame.font:
    font = pygame.font.Font(None, 36)
    text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
    textpos = text.get_rect(centerx=background.get_width()/2)
    background.blit(text, textpos)

while 1:
    clock.tick(60)

screen.blit(background, (0, 0))
pygame.display.flip()
time.sleep(10)