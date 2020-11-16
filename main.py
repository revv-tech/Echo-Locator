import pygame as pg
from random import randint
import pygame
from boundary import Boundary
from particle import Particle
from ray import Ray
from PIL import Image
import time

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

        
def main():
    ### CONFIG
    #start_time = time.time()
    global pixels
    screen_w = 500
    screen_h = 500
    border_on = True
    num_walls = 3
    segment = 0
    num_rays = 8
    rays2 = []
    white = (255,255,255)
    blue = (0, 0, 255)
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

    #BOUNDARIES
        
    # BLOQUE 1
    boundaries.append(Boundary(screen, (20, 85), (50, 30)))
    boundaries.append(Boundary(screen, (50, 30), (100, 30)))
    boundaries.append(Boundary(screen, (250, 30), (200, 30)))  
    boundaries.append(Boundary(screen, (10, 200), (50, 230)))
    boundaries.append(Boundary(screen, (130, 100), (170, 140)))
    boundaries.append(Boundary(screen, (150, 120), (100, 130)))

    # BLOQUE 2
    boundaries.append(Boundary(screen, (250, 30), (300, 10)))    
    boundaries.append(Boundary(screen, (450, 30), (495, 70)))
    boundaries.append(Boundary(screen, (350, 30), (400, 20)))
    boundaries.append(Boundary(screen, (495, 70), (495, 200)))
    boundaries.append(Boundary(screen, (495, 70), (495, 200)))
    boundaries.append(Boundary(screen, (495, 70), (495, 200)))
    boundaries.append(Boundary(screen, (320, 70), (270, 100)))
    boundaries.append(Boundary(screen, (410, 100), (390, 150)))
    boundaries.append(Boundary(screen, (410, 100), (340, 110)))

    # BLOQUE 3
    boundaries.append(Boundary(screen, (20, 400), (50,350)))
    boundaries.append(Boundary(screen, (20, 400), (60,370)))
    boundaries.append(Boundary(screen, (60, 370), (60,476)))
    boundaries.append(Boundary(screen, (80, 400), (60,476)))
    boundaries.append(Boundary(screen, (300, 485), (150,450)))
    boundaries.append(Boundary(screen, (90, 300), (50,250)))
    boundaries.append(Boundary(screen, (150, 390), (150,450)))

    # BLOQUE 4
    boundaries.append(Boundary(screen, (495, 495), (400,495)))
    boundaries.append(Boundary(screen, (300, 400), (400,495)))
    boundaries.append(Boundary(screen, (495, 300), (480,400)))
    boundaries.append(Boundary(screen, (400, 300), (330,360)))
    boundaries.append(Boundary(screen, (420, 320), (350,380)))
    boundaries.append(Boundary(screen, (440, 340), (370,400)))
    

 
    while running:
     
        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                
                #CAMBIAN LOS SECTORES
                if event.key == pygame.K_4:
                    pixels = []
                    screen.fill((0, 0, 0))
                    
                    for i in range(0, 20):
                        
                        segment = 0
                        rayCaster(segment, num_rays, pg.Vector2(250, 250), screen, boundaries, p, 0)
                        
                        for pix in pixels:
                            #PIX = PIX[0] => PIXEL, PIX[1] = COLOR
                            pos = pix[0]
                            color = pix[1]
                            #print(pix)
                            drawline(screen, color, pos, pos, 1)


                        drawline(screen, blue, (250, 250), (500, 250), 1)
                        drawline(screen, blue, (250, 250), (250, 500), 1)
                        p.update(screen)
                        pg.display.update()
                        pg.time.wait(75)
                    #print("--- %s seconds ---" % (time.time() - start_time))
                elif event.key == pygame.K_1:
                    pixels = []
                    screen.fill((0, 0, 0))
                    
                    for i in range(0, 20):
                        
                        segment = 180
                        rayCaster(segment, num_rays, pg.Vector2(250, 250), screen, boundaries, p, 0)
                        
                        for pix in pixels:
                            #PIX = PIX[0] => PIXEL, PIX[1] = COLOR
                            pos = pix[0]
                            color = pix[1]
                            #print(pix)
                            drawline(screen, color, pos, pos, 1)

                        drawline(screen, blue, (250, 250), (250, 0), 1)
                        drawline(screen, blue, (250, 250), (0, 250), 1)
                        p.update(screen)
                        pg.display.update()
                        pg.time.wait(75)
                    #print("--- %s seconds ---" % (time.time() - start_time))
                    
                elif event.key == pygame.K_2:
                    pixels = []
                    screen.fill((0, 0, 0))
                    for i in range(0, 20):
                        
                        segment = 270
                        rayCaster(segment, num_rays, pg.Vector2(250, 250), screen, boundaries, p, 0)
                        
                        for pix in pixels:
                            #PIX = PIX[0] => PIXEL, PIX[1] = COLOR
                            pos = pix[0]
                            color = pix[1]
                            #print(pix)
                            drawline(screen, color, pos, pos, 1)

                        drawline(screen, blue, (250, 250), (250, 0), 1)
                        drawline(screen, blue, (250, 250), (500, 250), 1)                           
                        p.update(screen)
                        pg.display.update()
                        pg.time.wait(75)
                    #print("--- %s seconds ---" % (time.time() - start_time))
                    
                elif event.key == pygame.K_3:
                    pixels = []
                    screen.fill((0, 0, 0))
                    for i in range(0, 20):
                        
                        segment = 90
                        rayCaster(segment, num_rays, pg.Vector2(250, 250), screen, boundaries, p, 0)
                        
                        for pix in pixels:
                            #PIX = PIX[0] => PIXEL, PIX[1] = COLOR
                            pos = pix[0]
                            color = pix[1]
                            #print(pix)
                            drawline(screen, color, pos, pos, 1)

                        drawline(screen, blue, (250, 250), (0, 250), 1)
                        drawline(screen, blue, (250, 250), (250, 500), 1)                             
                        p.update(screen)
                        pg.display.update()
                        pg.time.wait(75)
                    #print("--- %s seconds ---" % (time.time() - start_time))
            
def rayCaster(segment, num_rays, start, screen, boundaries, p, bounce):
    
    global pixels
    
    if bounce == 3:
        return
    
    num_second = 0
    result = rayEditor(segment, num_rays, start, 4)
    rays = result[0]
    secondaries = result[1]
   
    for b in boundaries:
        b.update(screen)

    for i in range(0, len(rays)):
        
        rays[i].update(screen, boundaries)
        
        if num_second > 0:
            
            secondaries[i][0].update(screen, boundaries)
            secondaries[i][1].update(screen, boundaries)
  
    pixels = pixels + getPixels(rays,[],bounce)

    pixs = getDirectPix(rays, secondaries, screen, boundaries)
    
    for i in range(0, len(pixs)):

        for j in range(0, len(secondaries[i])):
            
            if pixs[i] != []:
                pixel = getClosestPixel(pixs[i], secondaries[i][j],bounce)
                pixels = pixels + [pixel]
    
    for i in range(0, len(rays)):

        rayCaster(rays[i].heading + 180, num_rays, pg.Vector2(rays[i].end.x, rays[i].end.y), screen, boundaries, p, bounce+1)

        
def getClosestPixel(lista, ray, bounce):

    distances = []

    for pix in lista:

        dist = ray.start.distance_to(pix)
        distances.append(dist)

    closest = 100000000
    index = 0
    
    for i in range(0, len(distances)):

        diff = abs(distances[i] - ray.dist)
        if  diff < closest:

            closest = diff
            index = i
            
    #Calculo de Intensidad
    color = getIntensidad(ray.dist,bounce,True)
    #Elemento de Lista Pixeles
    elem = [lista[index],color]
    return elem

#OBTIENE LISTA DE PIXELES DE RAYOS PRIMARIOS
def getPixels(rays, pixList,bounce):
    
    if not rays:
        return pixList
    else:
        #Ubicacion del pixel
        pix = (rays[0].end.x,rays[0].end.y)
        #Calculo de intensidad
        intensidad = getIntensidad(rays[0].dist,bounce)
        #ELEMENTO DE LISTA
        fullPixel = [pix] + [intensidad]
        
        if pix not in pixels:
            return getPixels(rays[1:],pixList + [fullPixel],bounce)
        else:
            return getPixels(rays[1:],pixList,bounce)
        
#OBTENER INTESIDAD
def getIntensidad(distance,bounce,flagSecondary = False):

    intensidad = (1-(distance/500))**2
    intensidad = max(0, min(intensidad, 255))
    intensidad =  (255 * intensidad)
    
    if intensidad > 255:
        intensidad = 255
        
    if bounce == 0:
        color = (intensidad,intensidad,intensidad)
        return color
    #Calcula la intensidad de acuerdo al rebote
    intensidad = intensidad - (intensidad * (bounce/100))
    #Cada vez que sea un rayo secundario disminuye su intensidad un 25%
    if flagSecondary:
        intensidad = intensidad - (intensidad * 0.25)
    return (intensidad,intensidad,intensidad)

#OBTENER PICS DE LOS SECUNDARIOS
def getDirectPix(rays, secondaries, screen, boundaries):

    temp = []
    pixList = []
    for ray in rays:

        temp.append(Ray(ray.end, ray.heading, True))

    for ray in temp:

        ray.update(screen, boundaries)

    for ray in temp:

        pt1 = (int(ray.start.x), int(ray.start.y))
        pt2 = (int(ray.end.x), int(ray.end.y))
        result = get_points(int(ray.start.x), int(ray.start.y), int(ray.end.x), int(ray.end.y))
        
        if pt1 in result:
            result.remove(pt1)

        if pt2 in result:
            result.remove(pt2)
            
        pixList += [result]

    return pixList

    

                             
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


    

    
