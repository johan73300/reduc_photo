# Réduction de toutes les photos d'un dossier

Ce programme consiste à réduire la taille de toutes les images d'un dossier.  
Cela crée un dossier \<dossier\>\_reduc\_\<pourcentage\> et copie toutes les photos réduites dans celui-ci.  
Pour cela, le programme utilise la commande **convert** du package **ImageMagick**.



## Commande
```sh
./reduc_image.py -d <dossier> -p <pourcentage>
```
Dossier : chemin relatif ou chemin absolu  
Pourcentage : Taille de l'image * pourcentage / 100

