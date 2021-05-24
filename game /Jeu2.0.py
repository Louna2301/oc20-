import pygame
pygame.init()

# classe jeu
class Game:
    
    def __init__(self):
        # definir si notre jeu a commencé
        self.is_playing = False

# fenetre du jeu
pygame.display.set_caption('Pong') 
screen = pygame.display.set_mode((1080, 720))

# arrière plan du jeu
background = pygame.image.load('images2.0/background.png')

pygame.quit()