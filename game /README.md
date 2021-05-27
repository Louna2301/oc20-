# Game
# Pong
## Présentation du jeu
Notre jeu consiste à mettre un personnage, Mario, face à des monstres tels que des Goomba. A l'aide de ses munitions en forme de carapaces, sa mission sera de vaincre ces montres. Un Goomba tué lui fera remporter 20 points. A certains momens du jeu, les ennemis ne seront plus des Goomba, mais une pluie de boules piquantes (Pic-pic), cette apparition va venir compliquer la situation de notre Mario. Au-dessus de chaque personnages, il y aura une barre de vie, ainsi, nous pourrons regarder l'état du joueur, ainsi que ceux des ennemis. En bas de l'écran, une barre se remplit au fur et à mesure que le jeu avance: elle sert à pour nous prévenir quand arrivera la pluie de Pic-pic. 

Les commandes que nous devrons utiliser sont :
* ➡️ : avancer en direction des ennemis ou esciver les Pic-pic
* ⬅️ : reculer
* ``espace``: tirer les carapaces

<img width="1192" alt="Capture d’écran 2021-04-19 à 18 41 10" src="https://user-images.githubusercontent.com/77683990/115272962-43f3e100-a13f-11eb-8844-157f84460fe5.png">

Sur cette image, nous voyons l'écran de départ du jeu, pour le mettre en marche, nous allons utiliser le ``MOUSEBUTTONDOWN`` (il suffit d'appuyer sur le bouton ``PLAY``avec la souris). Ceci permet ainsi de commencer le jeu. L'écran avec le titre disparaît et le personnage Mario va apparaître. 

<img width="1440" alt="Capture d’écran 2021-04-19 à 18 39 54" src="https://user-images.githubusercontent.com/77683990/115272981-481ffe80-a13f-11eb-9eb4-4d87cf8178fa.png">

Sur cette image, le jeu vient d'avoir été lancé. Le joueur, Mario (généré par la classe ``Player``), ainsi que ses adversaires, les Goomba (générés par la classe ``Monster``) viennent d'apparaître. Nous pouvons voir que la partie vient d'être lancée, car les barres de vie sont encore pleines (entièrement vertes), il n'y a encore eu aucune confrontation (aucune collision). Nous pouvons également le remarquer, car le score (inscrit en haut à gauche) est encore égal à 0. La barre en bas de l'écran, qui sert au déclanchement des pluie de Pic-pic (généré par la classe ``Comet``), est en train de se remplire, nous pouvons le remarquer, car elle devient de plus en plus rouge.

<img width="822" alt="Capture d’écran 2021-04-19 à 21 19 56" src="https://user-images.githubusercontent.com/77742973/115346900-0d56ae80-a1b1-11eb-810b-0676f19f496b.png">

Mario doit se défendre et pour cela, avec la classe ``Projectile``, il va pouvoir lancer des attaques sous forme de carapaces pour ainsi vaincre les Goomba. Pour pouvoir les activer, nous utilisons la touche ``espace``. Quand les carapaces vont rentrer en collision avec les monstres, leur barres de vie vont diminuer jusqu'à ce qu'il n'y ait plus rien: dans ce cas-là, ils meurent et disparaîssent. Mais faisons attention, d'autres monstres vont arriver avec des vitesses différentes. Arriverons-nous à gérer plusieurs Goomba à la fois ?? 

<img width="1440" alt="Capture d’écran 2021-04-19 à 18 41 18" src="https://user-images.githubusercontent.com/77683990/115273018-53732a00-a13f-11eb-9d14-69451be117ad.png">

Le jeu continue avec cette image. Cette fois-ci Mario et les Goomba ont commencé à s'affronter. Le score a augmenté. Il est maintenant à 20 point ce qui signifie que le joueur à réussi à éliminer un de ses adversaires (en effet chaque Goomba tué rapporte 20 points au joueur). Nous pouvons aussi appercevoir qu'un deuxième Goomba est en train de se faire vaincre par Mario. Sa barre de vie est en train de dimininuer, car il a dû entrer en collision avec une ou plusieurs carapaces. Les dégats sont infligés à l'adversaire au moyen de la méthode ``forward`` dès qu'une carapace entre en collision avec un Goomba, cela impacte la méthode ``damage`` et réduit la barre de vie de ce méchant. Cependant, Mario lui n'a pas encore subit d'attaque de la part des adversaires (sa barre de vie est encore pleine). Enfin, la barre du bas en toujours en cours de remplissage, la pluie de Pic-pic n'a pas encore eu lieu.

<img width="1440" alt="Capture d’écran 2021-04-19 à 18 43 30" src="https://user-images.githubusercontent.com/77683990/115273025-553ced80-a13f-11eb-9460-1008cb8f194b.png">

Une fois la barre inférieur de l'écran remplie de rouge, les Goomba vont disparaitre pour un moment, afin de laisser place à une pluie de Pic-pic. C'est une étape différente qu'une attaque de Goomba. Il ne pourra pas se défendre avec ses attaques carapaces et donc, il faudra qu'il se déplace à droite ou à gauche. Les méthodes `` move_right`` pour bouger à droite et ``move_left`` pour s'orienter vers la gauche, vont avoir une meilleure utilisation dans cette étape. Pour cela, nous utiliserons les touches ⬅️ et ➡️. Après avoir fait collision un Pic Pic, Mario perdera des points dans la barre de vie. C'est la même fonctionnalité que les collisions avec des Goomba. 

## Règles du jeu
Grâce aux munitions carapaces, allons aider Mario à survivre face au Goomba et aux pluies de Pic-Pic !  

Alors, quel sera notre score ? 

## Fin du jeu
Le jeu prend fin au moment où Mario n'a plus de vie.  

## Diagramme de classes
![Untitled Diagram](https://user-images.githubusercontent.com/77683990/115990029-6c596080-a5c1-11eb-8524-d0de85f317b0.png)

## Références
La base de notre jeu est inspiré de la série de vidéos ``Comment créer un jeu en python`` de ``Graven - Developpement``  https://www.youtube.com/channel/UCIHVyohXw6j2T-83-uLngEg

## Sources images/son
Palettes :

Balle :

Typo :

Background :
