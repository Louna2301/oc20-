# classe jeu
class Game:
    def __init__(self):
        # definir si notre jeu a commencé
        self.is_playing = False
        
    def start(self):
        self.is_playing = True

# classe palet
class Palet(pygame.sprite.Sprite):
     def __init__(self, game):
        super().__init__()
        self.game = game
        self.rect.x = 100
        self.rect.y = 525
        
    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
        
    def move_left(self):
        self.rect.x -= self.velocity

# classe balle
class Ball(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.rect.x = 100
        self.rect.y = 525