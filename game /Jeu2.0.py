import pygame
pygame.init()

# classe game
class Game:
    
    def __init__(self):
        # charger la palette de gauche
        self.palet1 = Palet1()
        self.pressed = {}
        # charger la palette de droite
        self.palet2 = Palet2()
        self.pressed = {}
         # charger la balle
        self.ball = Ball()
           
# classe palette de gauche
class Palet1(pygame.sprite.Sprite):
    
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

# classe palette de droite
class Palet2(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('images2.0/palet.png')
        self.image = pygame.transform.scale(self.image, (20, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 880
        self.rect.y = 50
        
    def move_up(self):
        self.rect.y -= self.velocity
        
    def move_down(self):
        self.rect.y += self.velocity
        
# classe balle
class Ball(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('images2.0/ball.png')
        self.image = pygame.transform.scale(self.image, (80, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
       
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
    
    # appliquer l'image de la palette de gauche
    screen.blit(game.palet1.image, game.palet1.rect)
    
    # verifier si le joueur veut aller en haut ou en bas avec la palette de gauche
    if game.pressed.get(pygame.K_e) and game.palet1.rect.y > 0:
        game.palet1.move_up()
    elif game.pressed.get(pygame.K_x) and game.palet1.rect.y < 570:
        game.palet1.move_down()
        
    # appliquer l'image de la palette de droite
    screen.blit(game.palet2.image, game.palet2.rect)
    
    # verifier si le joueur veut aller en haut ou en bas avec la palette de droite
    if game.pressed.get(pygame.K_i) and game.palet2.rect.y > 0:
        game.palet2.move_up()
    elif game.pressed.get(pygame.K_m) and game.palet2.rect.y < 570:
        game.palet2.move_down()
        
     # appliquer l'image de la balle
    screen.blit(game.ball.image, game.ball.rect)
    
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