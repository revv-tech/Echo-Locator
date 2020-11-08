import pygame as pg
from random import randint
import pygame
from boundary import Boundary
from particle import Particle
from ray import Ray
from PIL import Image

#AUXILIAR
#E: Lista de Rayos y un entero
#S: Una nueva lista de rayos
#D: Crea una nueva lista de rayos ubicados en otro sector
def rayEditor(segment,num_rays,p):
    rays = []
    for i in range(num_rays):
        
        x = randint(0, 90)
        rays.append(Ray(p, (x + segment) + 1, False))
        rays.append(Ray(p, (x + segment)))
        rays.append(Ray(p, (x + segment) - 1, False))
        
    return rays

#AUXILIAR
#E: Dos coordenadas
#S: No tiene
#D: Pinta los pixeles en la ventana
def pintaPixels(x, y):

    color = (0,172,193)

    icono = Image.open('img.png')
    icono = icono.convert("RGBA")

    pixels = icono.load()

    r, g, b, a = pixels[x, y]
    pixels[x, y] = (color[0], color[1], color[2], a)
    icono.save("img.png")
    
def main():
    ### CONFIG
    screen_w = 500
    screen_h = 500
    border_on = True
    num_walls = 3
    segment = 0
    num_rays = 100
    ### END CONFIG

    pg.init()
    screen = pg.display.set_mode((screen_w, screen_h))

    running = True
    pg.event.set_allowed([pg.QUIT, pg.KEYDOWN, pg.KEYUP])

    p = Particle()
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
    boundaries.append(Boundary(screen, (495, 200), (400, 250)))
    boundaries.append(Boundary(screen, (495, 70), (495, 200)))
    boundaries.append(Boundary(screen, (320, 70), (270, 100)))
    
    boundaries.append(Boundary(screen, (495, 495), (400,495)))
    boundaries.append(Boundary(screen, (300, 400), (400,495)))
    boundaries.append(Boundary(screen, (495, 350), (400,320)))
    boundaries.append(Boundary(screen, (495, 350), (450,400)))
    boundaries.append(Boundary(screen, (240, 320), (300,300)))
    boundaries.append(Boundary(screen, (190, 200), (150,200)))
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
                #EMPIEZA LA LISTA DE RAYOS
                if event.key == pygame.K_BACKSPACE:
                    rays = rayEditor(segment,num_rays,p)
                #CAMBIAN LOS SECTORES
                if event.key == pygame.K_4:
                    segment = 0
                    rays = rayEditor(segment,num_rays,p)
                if event.key == pygame.K_1:
                    segment = 90
                    rays = rayEditor(segment,num_rays,p)
                if event.key == pygame.K_2:
                    segment = 180
                    rays = rayEditor(segment,num_rays,p)
                if event.key == pygame.K_3:
                    segment = 270
                    rays = rayEditor(segment,num_rays,p)
                

            
        screen.fill((0, 0, 0))

        for b in boundaries:
            b.update(screen)

        
        for r in rays:
            r.update(screen, p, boundaries)

        
        p.update(screen)
        pg.display.update()
        pg.time.wait(75)


if __name__ == "__main__":
    main()


    

    
