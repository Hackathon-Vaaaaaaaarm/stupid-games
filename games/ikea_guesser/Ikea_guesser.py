# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 22:09:00 2020

@author: karlm
"""

import pygame
from playsound import playsound

pygame.init()

x = 600
y = 600
display = pygame.display.set_mode((x,y))

width = display.get_width()
height = display.get_height()

pygame.display.update()
pygame.display.set_caption('Ikea Guesser')

black = (0,0,0)
white = (255,255,255)
grey = (125,125,125)
dark_grey = (55,55,55)

mouse = [0,0]

filenames = ['BEKANT.png','FREIHETEN.png','IDASEN.png','MALM.png']
pictures = [pygame.image.load(file) for file in filenames]

for i, picture in enumerate(pictures):
    pictures[i] = pygame.transform.scale(picture,(400,400))

wrongnames = ['MARCUS','KLOEVRING', 'BAADNUNG','PHILLIP','MCGUEEN']

game_over = False

small_font = pygame.font.SysFont('Corbel',35)
text = small_font.render('Quit',True, black)

class button:
    def __init__(self, height, width, x , y):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.text = text
        self.right_button = right_button
        
    def get_domain(self):
        x_to_from =[self.x, self.x + self.width]
        y_to_from = [self.y, self.y + self.width]
        return x_to_from, y_to_from
    
    def update_text(self):
        display.blit(self.text, (self.x,self.y))

    
one_button = button(100,50,height-550,width-100)
one_button.text = small_font.render('Quit',True, black)

second_button = button(100,50,height-350,width-100)
second_button.text = small_font.render('Quit',True, black)

third_button = button(100,50,height-150,width-100)
third_button.text = small_font.render('Quit',True, black)

buttons = [one_button,second_button, third_button]

points = 0


while not game_over:
    display.fill(white)
    display.blit(pictures[0], (100,0))
    
    mouse = pygame.mouse.get_pos()

    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game_over = True 
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                x, y = button.get_domain()
                if x[0] <= mouse[0] <= x[1] and y[0] <= mouse[1] <= y[1] and button.right_button == True:
                    points = points + 1
                elif x[0] <= mouse[0] <= x[1] and y[0] <= mouse[1] <= y[1] and button.right_button == False:
                    points = points - 1
    for button in buttons:
        x, y = button.get_domain()
        if x[0] <= mouse[0] <= x[1] and y[0] <= mouse[1] <= y[1]:
            pygame.draw.rect(display,grey,[button.x,button.y,button.height,button.width])
        else:
            pygame.draw.rect(display,dark_grey,[button.x,button.y,button.height,button.width])
            
    for button in buttons:
        button.update_text()
        
        
        
    #display.blit(text, (quit_button.width,quit_button.height))
    pygame.display.update()
pygame.quit()
#quit()







    # Change colour if mouse over
    #if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
    #    pygame.draw.rect(display,grey,[width/2+50,height/2+50,200,400]) 
    # If not, draw default colour
    #else: 
#    pygame.draw.rect(display,dark_grey,[width/2+50,height/2+50,140,40])
