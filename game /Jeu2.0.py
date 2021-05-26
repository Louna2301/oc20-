import pygame
pygame.init()

# classe game
class Game:
    
    def __init__(self):
        # charger palette
        self.palet = Palet()
        self.pressed = {}
           
# classe palette
class Palet(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('images2.0/palet.png')
        self.image = pygame.transform.scale(self.image, (20, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        
    def move_up(self):
        self.rect.y -= self.velocity
        
    def move_down(self):
        self.rect.y += self.velocity
        
# fenetre du jeu
pygame.display.set_caption('Pong') 
screen = pygame.display.set_mode((950, 720))

# arrière plan du jeu
background = pygame.image.load('images2.0/background.png')

# charger le jeu
game = Game()

running = True

# boucle tant que la condition est vrai
while running:
    
    # appliquer l'arriere plan du jeu
    screen.blit(background, (-5, 0))
    
    # appliquer l'image de la palette
    screen.blit(game.palet.image, game.palet.rect)
    
    # verifier si le joueur veut aller en haut ou en bas
    if game.pressed.get(pygame.K_i) and game.palet.rect.y > 0:
        game.palet.move_up()
    elif game.pressed.get(pygame.K_m) and game.palet.rect.y < 570:
        game.palet.move_down()
        
    print(game.palet.rect.y)
    
    # mettre a jour l'ecran
    pygame.display.flip()
    
    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # evenement est la fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        # si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
                      