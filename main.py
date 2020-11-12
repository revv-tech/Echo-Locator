import pygame as pg
from random import randint
import pygame
from boundary import Boundary
from particle import Particle
from ray import Ray
from PIL import Image

drawline = pg.draw.line
rays = []
pixels = []
#AUXILIAR
#E: Lista de Rayos y un entero
#S: Una nueva lista de rayos
#D: Crea una nueva lista de rayos ubicados en otro sector
def rayEditor(segment, num_rays, start):
    rays = []
    for i in range(num_rays):
        
        x = randint(0, 90)
        #rays.append(Ray(start, (x + segment) + 1, False))
        rays.append(Ray(start, (x + segment)))
        #rays.append(Ray(start, (x + segment) - 1, False))

    return rays

def getPixels(rays,pixList):
    
    if not rays:
        return pixList
    else:
        pix = (rays[0].end.x,rays[0].end.y)
        
        if pix not in pixels:
            return getPixels(rays[1:],pixList + [pix])
        else:
            return getPixels(rays[1:],pixList)
        
def main():
    ### CONFIG
    screen_w = 500
    screen_h = 500
    border_on = True
    num_walls = 3
    segment = 0
    num_rays = 10
    rays2 = []
    white = (255,255,255)
    #global rays
    ### END CONFIG

    pg.init()
    screen = pg.display.set_mode((screen_w, screen_h))

    running = True
    pg.event.set_allowed([pg.QUIT, pg.KEYDOWN, pg.KEYUP])

    p = Particle(pg.Vector2(250,250))
    p3 = Particle(pg.Vector2(0, 0))
    boundaries = []
    rays = []

    if border_on:
        boundaries.append(Boundary(screen, (0, 0), (screen_w, 0)))
        boundaries.append(Boundary(screen, (screen_w, 0), (screen_w, screen_h)))
        boundaries.append(Boundary(screen, (screen_w, screen_h), (0, screen_h)))
        boundaries.append(Boundary(screen, (0, screen_h), (0, 0)))

     #BOUNDERIES
    boundaries.append(Boundary(screen, (20, 85), (50, 30)))
    boundaries.append(Boundary(screen, (50, 30), (100, 30)))
    boundaries.append(Boundary(screen, (250, 30), (200, 30)))
    boundaries.append(Boundary(screen, (250, 30), (300, 10)))
    boundaries.append(Boundary(screen, (10, 200), (50, 230)))    
    boundaries.append(Boundary(screen, (450, 30), (495, 70)))
    boundaries.append(Boundary(screen, (350, 30), (400, 20)))
    boundaries.append(Boundary(screen, (495, 70), (495, 200)))
    boundaries.append(Boundary(screen, (495, 70), (495, 200)))
    #boundaries.append(Boundary(screen, (495, 200), (400, 250)))
    boundaries.append(Boundary(screen, (495, 70), (495, 200)))
    boundaries.append(Boundary(screen, (320, 70), (270, 100)))
    
    boundaries.append(Boundary(screen, (495, 495), (400,495)))
    boundaries.append(Boundary(screen, (300, 400), (400,495)))
    #boundaries.append(Boundary(screen, (495, 350), (450,320)))
    boundaries.append(Boundary(screen, (495, 350), (450,400)))
    #boundaries.append(Boundary(screen, (240, 320), (300,300)))
    #boundaries.append(Boundary(screen, (190, 200), (150,200)))
    boundaries.append(Boundary(screen, (20, 400), (50,350)))
    boundaries.append(Boundary(screen, (20, 400), (60,370)))
    boundaries.append(Boundary(screen, (60, 370), (60,476)))
    boundaries.append(Boundary(screen, (80, 400), (60,476)))
    boundaries.append(Boundary(screen, (150, 390), (150,450)))
    boundaries.append(Boundary(screen, (300, 485), (150,450)))
    boundaries.append(Boundary(screen, (90, 300), (50,250)))
 
    while running:
     
        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                
                #CAMBIAN LOS SECTORES
                if event.key == pygame.K_4:

                    for i in range(0, 20):
                        segment = 0
                        screen.fill((0, 0, 0))
                        rayCaster(segment, num_rays, pg.Vector2(250, 250), screen, boundaries, p, 0)
                        p.update(screen)
                        pg.display.update()
                        pg.time.wait(75)
                    
                elif event.key == pygame.K_1:
                    
                    for i in range(0, 20):
                        segment = 0
                        screen.fill((0, 0, 0))
                        rayCaster(segment, num_rays, pg.Vector2(250, 250), screen, boundaries, p, 0)
                        p.update(screen)
                        pg.display.update()
                        pg.time.wait(75)
                    
                elif event.key == pygame.K_2:
                    
                    for i in range(0, 20):
                        segment = 0
                        screen.fill((0, 0, 0))
                        rayCaster(segment, num_rays, pg.Vector2(250, 250), screen, boundaries, p, 0)
                        p.update(screen)
                        pg.display.update()
                        pg.time.wait(75)
                    
                elif event.key == pygame.K_3:
                    screen.fill((0, 0, 0))
                    for i in range(0, 20):
                        segment = 0
                        
                        rayCaster(segment, num_rays, pg.Vector2(250, 250), screen, boundaries, p, 0)

                        
                        
                        for pix in pixels:
                            drawline(screen, white, pix, pix, 1)
                            
                        p.update(screen)
                        pg.display.update()
                        pg.time.wait(75)

def rayCaster(segment, num_rays, start, screen, boundaries, p, bounce):
    global pixels
    
    if bounce == 3:
        return
    
    rays = rayEditor(segment, num_rays, start)
                            
    for b in boundaries:
        b.update(screen)
                            
    for ray in rays:
        ray.update(screen, boundaries)

    pixels = pixels + getPixels(rays,[])
    
    for i in range(0, len(rays)):

        rayCaster(rays[i].heading + 180, num_rays, pg.Vector2(rays[i].end.x, rays[i].end.y), screen, boundaries, p, bounce+1)
                             
                                
                   


if __name__ == "__main__":
    main()


    

    
