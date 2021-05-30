# Game
# Pong
## Présentation du jeu
Le ``Pong``est un des premier jeu vidéo apparu dans les années 70. Il est aujourd'hui concidéreé comme le commencement de l'industrie des jeux vidéos. Nous avons choisi de faire ce jeu vidéo, car malgré sa simplicité, il regroupe toute les notions importante dans la création d'un jeu vidéo. En plus de cela, c'est un moyen de redonner une nouvelle vie et de nous réapproprier cet "ancètre des jeux vidéo".
Equipé d'une raquette et d'uen balle, les joueurs s'affrontent dans le but de marquer le plus de points. Le point est gagné, lorsque la balle passe dans le but de l'autre, car celui-ci n'a pas réussi à rattrapper la balle avec sa raquette. Le jeu initial est conçu pour que le joueur ait le choix de jouer soit seul (contre un ordinateur), soit contre un réel adversaire. Dans le cas de notre jeu, les deux adversaires s'affronte sur un même ordinateur avec chacun sont côté du clavier.

Les commandes que nous devrons utiliser sont :

Pour le joueur de droite:
* ``i``: monter 
* ``m`` : descendre

Pour le joueur de gauche:
* ``e``: monter 
* ``x``: descendre 

### Captures d'écran

<img width="1201" alt="Capture d’écran 2021-05-30 à 16 50 39" src="https://user-images.githubusercontent.com/77683990/120108863-49454200-c167-11eb-90da-8a1d29c0a6b4.png">

Cette photo représente l'écran d'accueil de notre jeu vidéo. Nous avons dessiné la bannière ``PONG``, ainsi que le boutton ``PLAY`` sur lequel nous devons cliquer avec la souris, pour démarrer le jeu.

## Règles du jeu
Les règles du jeu sont simples:

Faites rebondire la balle sur votre raquette, feintez votre adversaire et soyez le premier à atteindre les 10 points sur le compteur de score.

Alors, qui aura le plus de points ??

## Fin du jeu
Le jeu se termine lorsqu'une personne arrive à atteindre les 10 points.

## Les classes
Dans ce jeu, il n'y a pas beaucoup de classe.

Il y a tout d'abord, la classe ``Sprite`` qui est la classe qui fait hériter tous les élémemts du jeu.

Il y ensuite, la classe ``Game`` qui continent tout les éléments du jeu.

Et enfin, les classes héritées de ``Sprite`` telles que la classe ``Palet1``, la classe ``Palet2`` et enfin, la classe ``Ball`` . Qui sont les éléments constituant le jeu vidéo.

## Le diagramme de classe

## Références et inspirations
La base de notre jeu est inspiré de la série de vidéos ``Comment créer un jeu en python`` de ``Graven - Developpement``  https://www.youtube.com/channel/UCIHVyohXw6j2T-83-uLngEg

## Sources images/son
Palettes : https://yorkdojo.github.io/worksheets/scratch/pong/, consulté le 26.05.2021

Balle : https://emojiterra.com/fr/rond-rouge/, consulté le 27.05.2021

Background : https://yorkdojo.github.io/worksheets/scratch/pong/, consulté le 26.05.2021
