import random
import math
import pygame, sys


G = 10
class Planet:
    def __init__(self, p_radius, x, y):
        self.prev_x = x
        self.prev_y = y
        self.x = x
        self.y = y
        self.radius = p_radius
        self.mass = self.radius * 2

    def force_mov(self, mass, r_x, r_y):
        hyp = (self.x - r_x)**2 + (self.y - r_y)**2
        theta = math.atan2(self.y - r_y, self.x - r_x)
        force = (G * self.mass * mass) / hyp * 10
        force_x = force*math.cos(theta)
        force_y = force*math.sin(theta)
        self.x -= force_x 
        self.y -= force_y 

    def draw_circle(self, display, color):
        return pygame.draw.circle(display, color, (self.x, self.y), self.radius)

class rand_planet:
    k = -math.sin(60)
    def __init__(self, r_x, r_y) -> None:
        self.x = r_x
        self.y = r_y
        self.radius = random.randrange(40,70)
        self.mass = float(self.radius * 2)
        self.color = tuple([random.randrange(1,125) for _ in range(3)])
        self.rect_x, self.rect_y = self.x - (self.radius * self.k),  self.y - (self.radius * self.k)
        self.rect = pygame.Rect(self.rect_x, self.rect_y, self.radius * self.k * 3, self.radius * self.k * 3 )
    
    #Draws a circle when called     
    def draw_circle(self,display):
        return pygame.draw.circle(display, self.color, (self.x, self.y),self.radius)