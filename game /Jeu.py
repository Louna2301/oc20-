import pygame
pygame.init()

# class jeu
class Game:
    
    def __init__(self):
        #generer notre joueur
        self.player = Player()
        self.pressed = {}
     

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
        self.rect.x = 100
        self.rect.y = 100
    
    def move_right(self):
        self.rect.x += self.velocity
        
    def move_left(self):
        self.rect.x -= self.velocity
     
# fenetre du jeu
pygame.display.set_caption('game') 
screen = pygame.display.set_mode((1080, 720))


# arrière plan du jeu
background = pygame.image.load('image/mariopaysage.jpg')

# charger notre jeu
game = Game()

# charger notre joueur
player= Player()

running = True

# boucle tant que running est vrai 
while running:
    
    # appliquer l'arrière plan
    screen.blit(background, (-500,-1145))
    
    # appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)
    
    # verifier si le joueur souhaite aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x:
        game.player.move_left()
    
    # mettre à jour l'ecran
    pygame.display.flip()
    
    # si on ferme la fenetre
    for event in pygame.event.get():
        # evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # si un joueur appuie sur une touche
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game.player.move_right()
            elif event.key == pygame.K_LEFT:
                game.player.move_left()
                
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
                            
            