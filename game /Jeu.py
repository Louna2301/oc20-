import pygame
pygame.init()

# classe joueur
class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('image/mario.png')
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 500
 
# fenetre du jeu
pygame.display.set_caption('game') 
screen = pygame.display.set_mode((1080, 720))


# arrière plan du jeu
background = pygame.image.load('image/mariopaysage.jpg')

# charger le joueur
player = Player

running = True

# boucle tant que running est vrai 
while running:
    
    # appliquer l'arrière plan
    screen.blit(background, (-500,-1145))
    
    # appliquer l'image du joueur
    screen.blit(player.image, image.rect)
    
    # mettre à jour l'ecran
    pygame.display.flip()
    
    # si on ferme la fenetre
    for event in pygame.event.get():
        # evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()