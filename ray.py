from particle import Particle
import pygame as pg
import decimal

drawline = pg.draw.line


class Ray:
    #E: SONAR, ANGULO(Heading), FLAG VERIFICADOR DE PRIMARIO
    def __init__(self, p: Particle, heading: float = 0, flagPrimary: bool = True):
        self.start = p.pos
        self.heading = heading
        self.end: pg.math.Vector2 = pg.math.Vector2()
        self.image = None
        self.flagPrimary = flagPrimary
    

    def update(self, screen: pg.display, p: Particle, boundaries: list):

        colorP = (100,100,100)
        colorS = (100, 50, 100)
        self.start = p.pos
        #print(p.pos)
        self.end.from_polar((10000, self.heading))

        closest = float("inf")
        new_end = pg.Vector2()

        x3 = self.start.x
        x4 = self.end.x
        y3 = self.start.y
        y4 = self.end.y

        for b in boundaries:
            x1 = b.start.x
            x2 = b.end.x
            y1 = b.start.y
            y2 = b.end.y

            den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if den == 0:
                return

            t_num = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
            t = t_num / den
            u_num = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3))
            u = u_num / den

            if u >= 0 and 0 <= t <= 1:
                x = x1 + t * (x2 - x1)
                y = y1 + t * (y2 - y1)
                dist = self.start.distance_to((x, y))
                if dist < closest:
                    closest = dist
                    new_end.xy = x, y

        if closest == float("inf"):
            self.end = self.start
            self.image = None
        else:
            self.end = new_end
            if self.flagPrimary:
                
                self.image = drawline(screen, colorP, self.start, self.end, 1) # COLOR
                
            else:
                self.image = drawline(screen, colorS, self.start, self.end, 1) # COLOR

    
a1 = decimal.Decimal(input('a1: '))
b1 = decimal.Decimal(input('b1: '))
c1 = decimal.Decimal(input('c1: '))
 
a2 = decimal.Decimal(input('a2: '))
b2 = decimal.Decimal(input('b2: '))
c2 = decimal.Decimal(input('c2: '))
def pinta_ecuacion(a, b, c):
    dev = ''
    if a != 0:
        dev += '%sx' % a
    if b > 0:
        dev += ' + %sy ' % b
    elif b < 0:
        dev += ' %sy ' % b
    dev += ' = %s' % c
 
    return dev
 
print(pinta_ecuacion(a1, b1, c1))
print(pinta_ecuacion(a2, b2, c2))
 
numerador_y = a2*c1 - a1*c2
denominador_y = a2*b1 - a1*b2
 
# método ce cálculo de la posición de rectas:
paralelas = a1*b2 == a2*b1
if paralelas:
    coincidentes = a1*c2 == a2*c1
    if coincidentes:
        print('Rectas coincidentes')
    else:
        print('Rectas paralelas')
else:
    # son secantes. calculo el punto de intersección
    if a1 == 0:
        y = c1/b1
        x = (c2-b2*y)/a2
    else:
        y = numerador_y/denominador_y
        x = (c1-b1*y)/a1
 
    print('Punto intersección: (%s, %s)' % (x, y))
    
