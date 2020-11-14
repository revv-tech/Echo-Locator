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
def rayEditor(segment, num_rays, start, num_second):
    
    rays = []
    second = []
    
    for i in range(num_rays):
        
        x = randint(0, 90)
        rays.append(Ray(start, (x + segment)))
        lista = []
        for i in range(0, num_second):
            lista.append(Ray(start, (x + segment) + (i+1), False))
            lista.append(Ray(start, (x + segment) + (i-1), False))

        second.append(lista)

    return [rays, second]

def getPixels(rays, pixList):
    
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
    num_rays = 1
    rays2 = []
    white = (255,255,255)
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
    
    num_second = 0
    result = rayEditor(segment, num_rays, start, num_second)
    rays = result[0]
    secondaries = result[1]
    
    for b in boundaries:
        b.update(screen)

    for i in range(0, len(rays)):
        
        rays[i].update(screen, boundaries)

        if num_second > 0:
            secondaries[i][0].update(screen, boundaries)
            secondaries[i][1].update(screen, boundaries)
  
    pixels = pixels + getPixels(rays,[])

    getDirectPix(rays, secondaries, screen, boundaries)
    
    for i in range(0, len(rays)):

        rayCaster(rays[i].heading + 180, num_rays, pg.Vector2(rays[i].end.x, rays[i].end.y), screen, boundaries, p, bounce+1)
        

def getDirectPix(rays, secondaries, screen, boundaries):

    temp = []
    pixList = []
    for ray in rays:

        temp.append(Ray(ray.end, ray.heading, True))

    for ray in temp:

        ray.update(screen, boundaries)

    for ray in temp:

        result = get_points(int(ray.start.x), int(ray.start.y), int(ray.end.x), int(ray.end.y))
        pixList += [[result]]

                             
# E: 2 puntos
# S: Lista de puntos entre los puntos dados
def get_points(x1, y1, x2, y2):
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points

if __name__ == "__main__":
    main()


    

    
