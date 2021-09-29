import pygame, sys
from pygame.constants import K_n
from classes import Planet, rand_planet


#--------------------------------------


pygame.init()
clock = pygame.time.Clock()

        


#DISPLAY DATA
black = (0,0,0)
ivory = (255, 255, 240)
s_height ,s_width = 1000, 1200
screen = pygame.display.set_mode((s_width,s_height))

#MAIN PLANET DATA
x, y = s_height*0.6, s_width*0.4
p_radius = float(5)
planet_1 = Planet(p_radius,x,y)
G = 10


main_list = []
planet_list = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
        #IF the delete key is pressed, delete all planets on screen
        #except for the main planet
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:
                screen.fill(black)
                planet_list.clear()
                main_list.clear()

            if event.key == pygame.K_r:
                planet_1.x, planet_1.y = x, y
                for i in  main_list:
                    i.x = i.prev_x
                    i.y = i.prev_y
            elif event.key == K_n:
                n_x, n_y = pygame.mouse.get_pos()
                main_list.append(Planet(p_radius,n_x, n_y))
        
        #if LMB pressed, add planet object to list
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event)
                r_x, r_y = pygame.mouse.get_pos()
                planet_list.append(rand_planet(r_x, r_y))
            elif event.button == 3:
                if not planet_list: break
                screen.fill(black)
                planet_list.pop()
            
    
    screen.fill(black)
    planet_1.draw_circle(screen, ivory)
    for new in main_list: new.draw_circle(screen,ivory)
    print(planet_1.x,'-------', planet_1.y)
    #Iterate through list of planets
    for i in planet_list:
        i.draw_circle(screen)
        for new in main_list:
            #new.draw_circle(screen, ivory)
            new.force_mov(i.mass, i.x, i.y )
        planet_1.force_mov(i.mass, i.x, i.y )
    
    clock.tick(60)
    pygame.display.update()