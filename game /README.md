# Game
## Présentation du jeu
Notre jeu consiste à mettre un personnage, donc nous avons pris Mario, et le mettre face aux monstres tels que Goomba. A l'aide de ses munitions en forme de carapaces, sa mission sera ainsi de vaincre ses montres. Un Goomba tué lui donnera 20 points. A certains moment du jeu, l'ennemi ne sera plus des Goomba mais une pluie de boules piquantes (Pic-pic), cette apparition va venir compiquer la situation de notre Mario. Au-dessus de chaque personnages, il y aura une barre de vie, ainsi tu pourras regarder l'état du joueur comme ceux des ennemis. En bas, tu pourras remarquer une barre qui se remplira au fur et à mesure que le jeu avance: c'est pour te prévenir quand est-ce qu'il y aura un changement entre une attaque de Goomba ou une pluie de Pic-pic. Tu pourras te déplacer à droite et à gauche grâce au touche <- et -> et pour attaquer, la barre d'espace est utilisée.

<img width="1192" alt="Capture d’écran 2021-04-19 à 18 41 10" src="https://user-images.githubusercontent.com/77683990/115272962-43f3e100-a13f-11eb-8844-157f84460fe5.png">

Nous avons donc l'écran de départ (Super Mario Play), pour pouvoir commencer le jeu, nous allons utiliser le MOUSEBUTTONDOWN. Ceci permet ainsi de commencer le jeu. L'écran avec le titre disparaît et le personnage Mario va apparaître. 

<img width="1440" alt="Capture d’écran 2021-04-19 à 18 39 54" src="https://user-images.githubusercontent.com/77683990/115272981-481ffe80-a13f-11eb-9eb4-4d87cf8178fa.png">

Sur cette image, le jeu vient d'avoir été lancé. Le joueur, Mario (généré par la classe 'Player'), ainsi que ses adversaire, les Goomba (généré par la classe 'Monsteur') viennent d'apparaitre. Nous pouvons voir que la partie vient d'être lancée, car les barres de vie sont encore pleine (entièrement verte), il n'y a encore eu aucune confrontation (aucune collision). Nous pouvons également le remarquer, car le score (inscrit en haut à gauche) est encore égal à 0. La barre en bas de l'écran, qui sert au déclanchement des pluie de Pic-pic (généré par la classe 'Comet'), est en train de se remplire, nous pouvons le remarqué car elle devient de plus en plus rouge.

<img width="822" alt="Capture d’écran 2021-04-19 à 21 19 56" src="https://user-images.githubusercontent.com/77742973/115346900-0d56ae80-a1b1-11eb-810b-0676f19f496b.png">

Mario doit se défendre et pour cela, avec la classe 'Projectile', il va pouvoir lancer des attaques sous forme de carapace pour ainsi vaincre ces Goomba. Pour pouvoir les activer, utilisez la barre d'espace. Quand les carapaces vont rentrer en collision avec les monstres, leur barres de vies vont diminuer jusqu'à ce qu'il n'y ait plus rien: dans ce cas-là, ils meurent et disparaîssent. Mais faites attention, d'autres monstres vont arriver avec des vitesses différentes. Arrivez-vous à gérer plusieurs Goomba à la fois ?? 

<img width="1440" alt="Capture d’écran 2021-04-19 à 18 41 18" src="https://user-images.githubusercontent.com/77683990/115273018-53732a00-a13f-11eb-9d14-69451be117ad.png">

Le jeu continue avec cette image. Cette fois-ci Mario et les Goomba ont commencé à s'affronter. Le score a augmenté. Il est maintenant à 20 point ce qui signifie que le joueur à réussi à éliminer un de ses adversaires (en effet chaque Goomba tué rapporte 20 points au joueur). Nous pouvons aussi appercevoir qu'un deuxième Goomba est en train de se faire vaincre par Mario. Sa barre de vie est en train de dimininuer, car il a dû entrer en collision avec une ou plusieurs carapaces. Les dégats sont infligés à l'adversaire au moyen de la méthode 'forward' dès qu'une carapace entre en collision avec un Goomba, cela impacte la méthode 'damage' et réduit la barre de vie de ce méchant. Cependant, Mario lui n'a pas encore subit d'attaque de la part des adversaires (sa barre de vie est encore pleine). Enfin, la barre du bas en toujours en cours de remplissage, la pluie de Pic-pic n'a pas encore eu lieu.

<img width="1440" alt="Capture d’écran 2021-04-19 à 18 43 30" src="https://user-images.githubusercontent.com/77683990/115273025-553ced80-a13f-11eb-9460-1008cb8f194b.png">

Une fois la barre inférieur de l'écran remplie de rouge, les Goomba vont disparaitre pour un moment, afin de laisser place à une pluie de Pic-pic. C'est une étape différente qu'une attaque de Goomba. Il ne pourra pas se défendre avec ses attaques carapaces et donc, il faudra qu'il se déplace à droite ou à gauche. Les fonctions, move_right(self) pour bouger à droite et move_left(self) pour s'orienter vers la gauche, vont avoir une meilleure utilisation dans cette étape. Pour cela, utilisez les touches <- et ->. Après avoir un reçu un Pic Pic, Mario perdera des points dans la barre de vie. C'est la même fonctionnalité que les collisions avec des Goomba. 


## Règles du jeu
Grâce aux munitions carapaces, aide Mario à survivre face au Goomba et aux pluies de Pic-Pic. 

Alors, quel sera ton score ?? 

## Fin du jeu
Le jeu prend fin au moment où Mario n'a plus de vie.  

## Références
https://www.youtube.com/watch?v=lXwZAJkTr1k&t=313s

https://www.youtube.com/channel/UCIHVyohXw6j2T-83-uLngEg
