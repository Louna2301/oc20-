import pygame
import math
import random
pygame.init()

# classe jeu
class Game:
    
    def __init__(self):
        # definir si notre jeu a commencé
        self.is_playing = True
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.comet_event = CometFallEvent(self)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        
    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
        
    def game_over(self):
        #remettre le jeu à neuf, retirer les monstres, remettre le joueur à 100 de vie, jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        
    def update(self, screen):
        # appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)
    
        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)
        
        # actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)
    
        # recuperer les projectile
        for projectile in self.player.all_projectiles:
            projectile.move()
        
        # recuperer les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            
        # recuperer les cometes
        for comet in self.comet_event.all_comets:
            comet.fall()
        
        # appliquer les projectiles
        self.player.all_projectiles.draw(screen)
    
        # appliquer les monstres
        self.all_monsters.draw(screen)
        
        # appliquer l'ensemble des images de mon groupe de cometes
        self.comet_event.all_comets.draw(screen)
    
        # verifier si le joueur souhaite aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x:
            self.player.move_left()
        
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
        
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
      
# classe joueur
class Player(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('image/mario.png')
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 525
        
    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur n'a plus de point de vie
            self.game.game_over()
        
    def update_health_bar(self, surface):
        # dessin barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 40, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 40, self.rect.y - 10, self.health, 5])
        
    def launch_projectile(self):
        #creer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))
    
    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
        
    def move_left(self):
        self.rect.x -= self.velocity
        
# classe projectile
class Projectile(pygame.sprite.Sprite):
    
    # definir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load('image/carapace.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 205 
        self.rect.y = player.rect.y + 80
        self.origine_image = self.image
        self.angle = 0
        
    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center) 
        
    def remove(self):
        self.player.all_projectiles.remove(self)
        self.rotate()
        
    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #supprimer le projectile qui touche un monstre
            self.remove()
            # infliger des degats
            monster.damage(self.player.attack)
        
        if self.rect.x > 1080:
            #supprimer le projectile sorti de l'ecran
            self.remove()

# classe monstre
class Monster(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('image/bowser.png')
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 525
        self.velocity = random.randint(1, 3)
    
    def damage(self, amount):
        # Infliger les degats
        self.health -= amount
        
        # verifier si son nouveau nombre de points de vie est inferieur ou egal à 0
        if self.health <= 0:
            # Reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health
            
            # si la barre d'evenement est chargee au max
            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)
                
            self.game.comet_event.attempt_fall()
        
    def update_health_bar(self, surface):
        # dessin barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 40, self.rect.y, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 40, self.rect.y, self.health, 5])
          
    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            # infliger des degats (au joueur)
            self.game.player.damage(self.attack)

#classe evenement
class CometFallEvent:
    # lors du chargement -> créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        self.fall_mode = False
        
        # definir un groupe de sprite pour definir nos cometes
        self.all_comets = pygame.sprite.Group()
        
    def add_percent(self):
        self.percent +=  self.percent_speed / 100
        
    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent(self):
        self.percent = 0
        
    def meteor_fall(self):
        for i in range(1, 10):
            self.all_comets.add(Comet(self))
    
    def attempt_fall(self):
        # la jauge d'evenement est totalement chargee
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print('Pluie de cometes!!!')
            self.meteor_fall()
            self.fall_mode = True
        
    def update_bar(self, surface):
        
        # ajouter du pourcentage a la barre
        self.add_percent()
        
        
        # barre noir (arriere plan)
        pygame.draw.rect(surface, (0, 0, 0), [
                0, # axe x
                surface.get_height() - 20, # axe y
                surface.get_width(), # longueur fenetre
                10 # epaisseur de la barre
            ])
        # barre rouge (jauge d'evenement)
        pygame.draw.rect(surface, (187, 11, 11), [
                0, # axe x
                surface.get_height() - 20, # axe y
                (surface.get_width() / 100) * self.percent, # longueur fenetre
                10 # epaisseur de la barre
            ])
        
# classe comete
class Comet(pygame.sprite.Sprite):
    
    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load('image/piece.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = -random.randint(0, 800)
        self.comet_event = comet_event
        
    def remove(self):
        self.comet_event.all_comets.remove(self)
        
        #verifier si le nombre de cometes est de 0
        if len(self.comet_event.all_comets) == 0:
            #remettre la barre a 0
            self.comet_event.reset_percent()
            # apparaitre les deux premiers monstres
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()
        
    def fall(self):
        self.rect.y += self.velocity
        
        # ne tombe pas sur le sol
        if self.rect.y >= 500:
            print('sol')
            #retirer la piece
            self.remove()
            
            # si il n'y a plus de piece
            if len(self.comet_event.all_comets) == 0:
                print('evenement est fini')
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
            
        # verifier si la piece touche le joueur
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
            ):
                print('joueur touché')
                self.remove()
                # subir degats
                self.comet_event.game.player.damage(20)
        
# fenetre du jeu
pygame.display.set_caption('game') 
screen = pygame.display.set_mode((1080, 720))

# arrière plan du jeu
background = pygame.image.load('image/mariopaysage.jpg')

# importer notre banière
banner = pygame.image.load('image/banner.png')
banner = pygame.transform.scale(banner, (500, 400))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

#importer notre bouton pour lancer la partie
play_button = pygame.image.load('image/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger notre jeu
game = Game()

# charger notre joueur
player= Player(game)

running = True

# boucle tant que running est vrai 
while running:
    
    # appliquer l'arrière plan
    screen.blit(background, (-500,-1145))
    
    # verifier si notre jeu a commencé
    if game.is_playing:
        # declencher les instructions de la partie
        game.update(screen)
    # verifier si notre jeu n'a pas commencé
    else:
        # ajouter mon ecran de bienvenue
        screen.blit(play_button, (play_button_rect))
        screen.blit(banner, (banner_rect))
        
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
            
            # touche espace pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
            
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifier pour savoir si on appuie sur la souris
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode 'lancé'
                game.start()