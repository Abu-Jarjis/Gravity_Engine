import random
import math
import pygame, sys

clock = pygame.time.Clock()

G = 100
MAIN_LIST = []
PLANET_LIST = []
class Planet:
    def __init__(self, p_radius, x, y):
        self.prev_x = x
        self.prev_y = y
        self.x = x
        self.y = y
        self.radius = p_radius
        self.mass = self.radius * 2

    def force_mov(self, mass, r_x, r_y):
        hyp = (math.dist((self.x,self.y), (r_x, r_y)))**2 + 1
        theta = math.atan2(self.y - r_y ,self.x - r_x )
        force = (G * self.mass * mass) / hyp * 1
        force_x = force*math.cos(theta)    #v * math.cos(theta_2)
        force_y = force*math.sin(theta)   #v * math.sin(theta_2)
        self.x -= force_x 
        self.y -= force_y 
    def check_dist(self, r_x, r_y, r_radius):
        pass
        #if math.dist((self.x, self.y), (r_x, r_y)) < r_radius:
                    #MAIN_LIST.remove(self)

    def draw_circle(self, display, color):
        return pygame.draw.circle(display, color, (self.x, self.y), self.radius)
    def orbital_speed(self, mass):
        pass
        
        #hyp = (self.x - r_x)**2 + (self.y - r_y)**2
        #theta = math.atan2(self.y - r_y ,self.x - r_x )
        #force = (G * self.mass * mass) / hyp * 1
        #pass
    def get_event(self, event, planet_1, x, y):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                    planet_1.x, planet_1.y = x, y
                    for i in  MAIN_LIST:
                        i.x = i.prev_x
                        i.y = i.prev_y
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:
                    MAIN_LIST.clear()

class rand_planet:
    #k = -math.sin((math.pi/180)*60)
    def __init__(self, r_x, r_y) -> None:
        self.x = r_x
        self.y = r_y
        self.radius = random.randrange(40,70)
        self.mass = float(self.radius * 2)
        self.color = tuple([random.randrange(1,125) for _ in range(3)])
        #self.rect_x, self.rect_y = self.x - (self.radius * self.k),  self.y - (self.radius * self.k)
        #self.rect = pygame.Rect(self.rect_x, self.rect_y, self.radius * self.k * 3 , self.radius * self.k * 3  )
    #Draws a circle when called     
    def draw_circle(self,display):
        return pygame.draw.circle(display, self.color, (self.x, self.y),self.radius)

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    PLANET_LIST.clear()

        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(event)
                    r_x, r_y = pygame.mouse.get_pos()
                    PLANET_LIST.append(rand_planet(r_x, r_y))
                elif event.button == 3:
                    if not PLANET_LIST:return
                    PLANET_LIST.pop()
                if event.button == 4:
                    for i in PLANET_LIST:
                        if math.dist(pygame.mouse.get_pos(), (i.x,i.y)) < i.radius:
                            i.radius += 2
                            i.mass = float(i.radius * 2)
    
def main():
    #DISPLAY DATA
    black = (0,0,0)
    ivory = (255, 255, 240)
    s_height ,s_width = 1000, 1200
    screen = pygame.display.set_mode((s_width,s_height))

    #MAIN PLANET DATA
    x, y = s_height*0.6, s_width*0.4
    p_radius = float(5)
    planet_1 = Planet(p_radius,x,y)
    default_planet = rand_planet(x-50, y)


    
    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_n]:
            n_x, n_y = pygame.mouse.get_pos()
            MAIN_LIST.append(Planet(p_radius,n_x, n_y))
        
        for event in pygame.event.get():
            planet_1.get_event(event, planet_1, x, y)
            default_planet.get_event(event)
            
            if event.type == pygame.QUIT:
                sys.exit()
        
                
        #WHILE N is HELD, ADD MAIN PLANETS/PARTICLES
        
            


        screen.fill(black)
        planet_1.draw_circle(screen, ivory)
        for new in MAIN_LIST: new.draw_circle(screen,ivory)
        print(planet_1.x,'-------', planet_1.y)
        #Iterate through list of planets
        for i in PLANET_LIST:
            i.draw_circle(screen)
            for new in MAIN_LIST:
                new.force_mov(i.mass, i.x, i.y )
                new.orbital_speed(i.mass)
                new.check_dist(i.x,i.y,i.radius)
            planet_1.force_mov(i.mass, i.x, i.y )
        
        clock.tick(60)
        pygame.display.update()
