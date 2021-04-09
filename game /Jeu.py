import pygame
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
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('image/mario.png')
        self.image = pygame.transform.scale(self.image, (250, 250))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 435
        
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
        
        if self.player.game.check_collision(self, self.player.game.all_monsters):
            #supprimer le projectile qui touche un monstre
            self.remove()
        
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
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 390
        self.velocity = 3
        
    def update_health_bar(self, surface):
        # couleur barre de vie
        bar_color = (111, 210, 46)
        
        # position/largeur/épaisseur barre de vie
        bar_position = [self.rect.x + 40, self.rect.y, self.health, 5]
        
        # dessin barre de vie
        pygame.draw.rect(surface, bar_color, bar_position)
        
        
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