import pygame
import math
import random
import sys
pygame.init()

# classe game
class Game:
    
    def __init__(self):
        # definir si notre jeu a commencé
        self.is_playing = False
        # charger la palette de gauche
        self.all_palets = pygame.sprite.Group()
        self.palet1 = Palet1()
        self.all_palets.add(self.palet1)
        self.pressed = {}
        # charger la palette de droite
        self.palet2 = Palet2()
        self.pressed = {}
        # charger la balle
        self.ball = Ball(self)
        self.all_ball = pygame.sprite.Group()
        self.score = 0 
        self.score2 = 0
        
    def start(self):
        self.is_playing = True
    
    def add_score(self, points):
        self.score += points
    
    def add_score2(self, points):
        self.score2 += points
        
    def game_over(self):
        self.is_playing = False
        self.score = 0
        
    def update(self, screen):
        # afficher le score sur l'ecran
        font = pygame.font.SysFont('monospace', 100)
        score_text = font.render(f'{self.score}', 1, (255, 255, 255))
        screen.blit(score_text, (450, 350))
        
        font = pygame.font.SysFont('monospace', 100)
        score2_text = font.render(f'{self.score2}', 1, (255, 255, 255))
        screen.blit(score2_text, (685, 350))
                    
        # appliquer l'image de la palette de gauche
        screen.blit(self.palet1.image, self.palet1.rect)
    
        # verifier si le joueur veut aller en haut ou en bas avec la palette de gauche
        if self.pressed.get(pygame.K_e) and self.palet1.rect.y > 0:
            self.palet1.move_up()
        elif self.pressed.get(pygame.K_x) and self.palet1.rect.y < 650:
            self.palet1.move_down()
        
        # appliquer l'image de la palette de droite
        screen.blit(self.palet2.image, self.palet2.rect)
    
        # verifier si le joueur veut aller en haut ou en bas avec la palette de droite
        if self.pressed.get(pygame.K_i) and self.palet2.rect.y > 0:
            self.palet2.move_up()
        elif self.pressed.get(pygame.K_m) and self.palet2.rect.y < 650:
            self.palet2.move_down()
        
        # appliquer l'image de la balle
        screen.blit(self.ball.image, self.ball.rect)
        
    def check_collision(self, sprite, group):
        pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        return game.ball.bounce()
            
# classe palette de gauche
class Palet1(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('images2.0/palet.png')
        self.image = pygame.transform.scale(self.image, (20, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 100
        self.mask = pygame.mask.from_surface(self.image)
        
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
        self.rect.x = 1135
        self.rect.y = 100
        self.mask = pygame.mask.from_surface(self.image)
        
    def move_up(self):
        self.rect.y -= self.velocity
        
    def move_down(self):
        self.rect.y += self.velocity
        
# classe balle
class Ball(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.velocity_x = 5
        self.velocity_y = 5
        self.velocity = 5
        self.image = pygame.image.load('images2.0/ball02.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 400
        self.angle = 0

    def move_ball(self):
        # si la balle n'est pas en collision avec une palette
        if not self.game.check_collision(self, [self.game.ball, self.game.palet2]):
            self.rect.x += self.velocity_x
            self.rect.y += self.velocity_y
       
    def bounce(self):
         self.velocity = -self.velocity
        
# fenetre du jeu
pygame.display.set_caption('Pong') 
screen = pygame.display.set_mode((1200, 800))

# arrière plan du jeu
background = pygame.image.load('images2.0/background.png')
background = pygame.transform.scale(background, (1200, 800))

# importer notre banière
banner = pygame.image.load('images2.0/Pong.jpg')
banner = pygame.transform.scale(banner, (500, 200))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4 + 50)
banner_rect.y = math.ceil(screen.get_height() / 4)

#importer notre bouton pour lancer la partie
play_button = pygame.image.load('images2.0/play.jpg')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33 + 50)
play_button_rect.y = math.ceil(screen.get_height() / 2 + 50)

# charger le jeu
game = Game()

running = True

# Score
score = 0

# Score2
score2 = 0

# boucle tant que la condition est vrai
while running:
    
    # appliquer l'arriere plan du jeu
    screen.blit(background, (0, 0))
    
    # verifier si notre jeu à commencé ou non
    if game.is_playing:
        # declencher les instructions de la partie
        game.update(screen)
        # verifier si notre jeu n'a pas commencé
    else:
        # ajouter mon ecran de bienvenue
        screen.blit(play_button, (play_button_rect))
        screen.blit(banner, (banner_rect))
   
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
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifier pour savoir si on appuie sur la souris
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode 'lancé'
                game.start()
    
    # Vérifier si la balle entre en collision avec les 2 murs (supérieur et inférieur de l'écran)
    if game.ball.rect.y>800:
        game.ball.velocity_y = -game.ball.velocity_y
    if game.ball.rect.y<0:
        game.ball.velocity_y = -game.ball.velocity_y
    
    # Calculer le score
    if game.ball.rect.x <= 0:
        game.add_score2(1)
        # remettre la balle au centre
        game.ball.rect.x = 600
        game.ball.rect.y = 400
    # Calculer le score
    if game.ball.rect.x >= 1200:
        game.add_score(1)
        # remttre la balle au centre
        game.ball.rect.x = 600
        game.ball.rect.y = 400
        
    game.ball.move_ball()