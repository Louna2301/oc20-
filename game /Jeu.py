import pygame
import random
pygame.init()

# classe jeu
class Game:
    
    def __init__(self):
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        self.spawn_monster()
        
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
        self.attack = 5
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
        
    def update_health_bar(self, surface):
        # dessin barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 40, self.rect.y, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 40, self.rect.y, self.health, 5])
          
    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
            
# fenetre du jeu
pygame.display.set_caption('game') 
screen = pygame.display.set_mode((1080, 720))

# arrière plan du jeu
background = pygame.image.load('image/mariopaysage.jpg')

# charger notre jeu
game = Game()

# charger notre joueur
player= Player(game)

running = True

# boucle tant que running est vrai 
while running:
    
    # appliquer l'arrière plan
    screen.blit(background, (-500,-1145))
    
    # appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)
    
    # actualiser la barre de vie du joueur
    game.player.update_health_bar(screen)
    
    # recuperer les projectile
    for projectile in game.player.all_projectiles:
        projectile.move()
        
    # recuperer les monstres
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)
        
    # appliquer les projectiles
    game.player.all_projectiles.draw(screen)
    
    # appliquer les monstres
    game.all_monsters.draw(screen)
    
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
            
            # touche espace pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
            
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False