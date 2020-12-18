#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 19:29:45 2020

@author: antonjorg
"""

import pygame
import numpy as np

class Pong():
    
    textColor = (255, 255, 255) 
    goodColor = (0, 255, 0)
    badColor = (255, 0, 0)
    backgroundColor = (0, 0, 40)
    platformColor = (150, 150, 180)
    
    def __init__(self):
        self. height = 600
        self.width = 800
        
        self.score = 0
        pygame.init()
        # Set up game
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.rendering = False
        
        # Initiate paddles
        self.objects = (Paddle(self, 0), Paddle(self, 1), Ball(self))
        
        self.points = [0,0]
        
        self.reset()
        
    def reset(self):
        for obj in self.objects:
            obj.reset()
        
        # Program status
        self.game_over = False
        self.won = False
        
    def step(self, actions):
        # Step the rocket
        if not self.game_over:
            for obj, action in zip(self.objects[:2], actions):
                obj.step(action)
            # step ball
            self.objects[2].step()
        # Check if game is over
        
        # return observation, reward, done
        #reward = self.rocket.fuel if self.won else 0
        #return ((self.rocket.x, self.rocket.y, self.rocket.xspeed, self.rocket.yspeed), reward, self.game_over)                
                
    def init_render(self):
        self.screen = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption('Shitty Pong')
        self.background = pygame.Surface(self.screen.get_size())
        self.rendering = True
                
    def render(self):
        if not self.rendering:
            self.init_render()
            
        # Limit to 30 fps
        self.clock.tick(120)
     
        # Clear the screen
        self.screen.fill(self.backgroundColor)
        
        # Draw text

        # Draw game over or you won       
        

        # Draw platform
        
        # Draw sprites
        for obj in self.objects:
            obj.draw()
        #self.sprites.draw(self.screen)
        text = self.font.render("P1: {}       P2: {}".format(self.points[1], self.points[0]), True, self.textColor)
        self.screen.blit(text, (self.width/2-text.get_width()/2, 30))  
        
        # Display
        pygame.display.flip()

    def close(self):
        pygame.quit()
        

class Paddle():
    height = 100
    width = 20
 
    def __init__(self, parent, team):
        self.parent = parent
        self.team = team
        self.reset()
        
        # params
        self.speed = 3
    
    def reset(self):       
        # Position of rocket
        self.y = self.parent.height/2
        self.x = self.parent.width/10 + (1-self.team)*8*self.parent.width/10

 
    def step(self, action):
        # Unpack action
        self.down, self.up = action
        
        if self.up:
            self.y -= self.speed
        if self.down:
            self.y += self.speed
        
        # bounding
        self.x = min(self.x, self.parent.width - self.width/2)
        self.x = max(self.x, self.width/2)
        
        self.y = min(self.y, self.parent.height - self.height/2)
        self.y = max(self.y, self.height/2)
        
        
    def draw(self):
        x1 = self.x - Paddle.width/2
        y1 = self.y - Paddle.height/2
        
        pygame.draw.rect(self.parent.screen, self.parent.platformColor, 
                         pygame.Rect(x1,y1,Paddle.width,Paddle.height))
        

class Ball():
    radius = 20
    
    def __init__(self, parent):
        self.parent = parent
        
        # params
        self.hascollided = False
        self.collisiontimer = 0
        
        self.reset()
        
    def reset(self):       
        # Position of rocket
        self.y = self.parent.height/2
        self.x = self.parent.width/2
        
        self.speed = 2
    
        self.a = np.random.random()*2*np.pi
        self.xspeed = self.speed * np.cos(self.a)
        self.yspeed = self.speed * np.sin(self.a)
        
    def step(self):
        # bounding
        self.x += self.xspeed
        self.y += self.yspeed
        
        collided = False
        
        if self.y < self.radius or self.y > self.parent.height - self.radius:
            self.yspeed *= -1
            collided = True
    
        for paddle in self.parent.objects[:2]:
            if (abs(self.x - paddle.x) < self.radius + paddle.width/2) and \
               (abs(self.y - paddle.y) < self.radius + paddle.height/2):
                   
                   a = np.pi * (np.sign(self.xspeed) == 1)
                   
                   a += np.arctan(0.8*self.yspeed/self.xspeed)
                   
                   cx = self.parent.width/2 - self.x
                   cy = self.parent.height/2 - self.y
                   a += 0.3*np.arctan(cy/cx)
                    
                   
                   self.a = a
                   self.speed += (10 - self.speed)*0.05
                   self.xspeed = self.speed * np.cos(self.a)
                   self.yspeed = -self.speed * np.sin(self.a)
                   collided = True
                   
        if self.x < -100:
            self.parent.points[0] += 1
            self.parent.reset()
            collided = True
        if self.x > self.parent.width + 100:
            self.parent.points[1] += 1
            self.parent.reset()
            collided = True
        
        if collided:
            self.parent.platformColor = random_color()
            self.parent.textColor = random_color()
            self.parent.backgroundColor = random_color()
        
    def draw(self):
        x1 = self.x - Paddle.width/2
        y1 = self.y - Paddle.height/2
        
        pygame.draw.circle(self.parent.screen, self.parent.platformColor, 
                         (self.x, self.y), Ball.radius)
        

def random_color():
    return tuple(np.random.randint(255, size=3))
        
if __name__ == "__main__":
    env = Pong()
    env.reset()
    exit_program = False
    
    actions = [[False, False], [False, False]]
    
    while not exit_program:
        env.render()
        env.step(actions) 
    
        # Process game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_program = True
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_ESCAPE, pygame.K_q]:
                    exit_program = True
                
                if event.key == pygame.K_r:
                    env.reset()
            
        keys = pygame.key.get_pressed() # It gets the states of all keyboard keys.
                
        # player 1 controls
        actions[1][1] = keys[ord('w')]
        actions[1][0] = keys[ord('s')]

        # player 0 controls
        actions[0][1] = keys[ord('i')]
        actions[0][0] = keys[ord('k')]
                
    env.close()    
        