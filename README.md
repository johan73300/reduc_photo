# Réduction de toutes les photos d'un dossier

Ce programme consiste à réduire la taille de toutes les images d'un dossier.  
Cela crée un dossier \<dossier\>\_reduc\_\<pourcentage\> et copie toutes les photos réduites dans celui-ci.  
Pour cela, le programme utilise la commande des commandes du package **Pillow**.

## Package nécessaires
Le programme utilise des fonction de Pillow.
Vous pouvez l'installer avec **pip**.

## Commande

### Réduction en fonction d'un pourcentage
```sh
./reduc_image.py -d <dossier> -p <pourcentage>
```
* Dossier : chemin relatif ou chemin absolu  
* Pourcentage : Taille de l'image * pourcentage / 100

### Réduction en fonction de la taille du plus grand côté :
```sh
./reduc_image.py -d <dossier> -m <plus_grand_cote>
```
* Dossier : chemin relatif ou chemin absolu  
* plus_grand_cote : Taille du plus grand côté


## Aide
```sh
usage: reduc_image.py [-h] [-d DIRECTORY] [-p PERCENTAGE | -m MAX_SIDE]

Decrease size of picture of one directory

optional arguments:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        name of directory
  -p PERCENTAGE, --percentage PERCENTAGE
                        percentage decrease
  -m MAX_SIDE, --max_side MAX_SIDE
                        Maximum side size
```