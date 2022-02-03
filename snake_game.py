
import pygame
import random
import os

class cuerpo:
    def __init__(self, ventana):
        self.x = 0
        self.y = 0
        self.dir = 0
        self.ventana = ventana
        
    def dibujar(self):
        pygame.draw.rect(self.ventana, (255, 255, 255), (self.x, self.y, 10, 10))
        
    def moverse(self):
        if self.dir == 0:
            self.x += 10
        elif self.dir == 1:
            self.x -= 10
        if self.dir == 2:
            self.y += 10
        elif self.dir == 3:
            self.y -= 10
            
class manazanas:
    def __init__(self, ventana):
        self.x = random.randrange(40)*10
        self.y = random.randrange(40)*10
        self.ventana = ventana
        
    def dibujar(self):
        pygame.draw.rect(self.ventana, (255, 0, 0), (self.x, self.y, 10, 10))
        
    def nueva_manzana(self):
        self.x = random.randrange(40)*10
        self.y = random.randrange(40)*10
            
def refrescar(ventana,var):
    pygame.font.init()
    fuente = pygame.font.Font(None, 20)
    mensaje = fuente.render("High Score "+ str(var), True, (255, 255, 255))
    ventana.fill((0, 0, 0))
    ventana.blit(mensaje, (150,10)) 
    comida.dibujar()
    for i in range(len(serpiente)):
        serpiente[i].dibujar()
    
    
def seguir_cabeza():
    for i in range(len(serpiente)-1):
        serpiente[len(serpiente) -i -1].x = serpiente[len(serpiente) -i -2].x
        serpiente[len(serpiente) -i -1].y = serpiente[len(serpiente) -i -2].y

def run():
    os.system("cls")
    global serpiente, comida
    pygame.display.set_caption("Snake Game")
    ventana = pygame.display.set_mode((400,400))
    ventana.fill((0,0,0))

    comida = manazanas(ventana)
    serpiente = [cuerpo(ventana)]
    run = True
    var = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and serpiente[0].dir != 1:
                    serpiente[0].dir = 0
                if event.key == pygame.K_LEFT and serpiente[0].dir != 0:
                    serpiente[0].dir = 1
                if event.key == pygame.K_DOWN and serpiente[0].dir != 3:
                    serpiente[0].dir = 2
                if event.key == pygame.K_UP and serpiente[0].dir != 2:
                    serpiente[0].dir = 3
        serpiente[0].moverse()
        refrescar(ventana,var)
        pygame.display.update()
        pygame.time.delay(100)
        
        if serpiente[0].x == comida.x and serpiente[0].y == comida.y:
            comida.nueva_manzana()
            serpiente.append(cuerpo(ventana))
            var += 1
        seguir_cabeza()
        
        if serpiente[0].x >= 400:
            serpiente[0].x = 0
        elif serpiente[0].x < 0:
            serpiente[0].x = 390
        if serpiente[0].y >= 400:
            serpiente[0].y = 0
        elif serpiente[0].y < 0:
            serpiente[0].y = 390

        
        
        
        

if __name__=='__main__':
    run()
    pygame.QUIT()