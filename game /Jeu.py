import pygame
pygame.init()

# fenetre du jeu
pygame.display.set_caption('game')
screen = pygame.display.set_mode((1080, 720))

# arrière plan du jeu
background = pygame.image.load('image/mariopaysage.jpg')

running = True

# boucle tant que running est vrai 
while running:
    
    # appliquer l'arrière plan
    screen.blit(background, (-500,-1145))
    
    # mettre à jour l'ecran
    pygame.display.flip()
    
    # si on ferme la fenetre
    for event in pygame.event.get():
        # evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()