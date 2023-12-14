


# PROJET MLOPS

## Professeur: Mr Fanilo
## Etudiant: Wendyam YAMEOGO
## Master: SISE

## Accessibilité 1: 
### Lien API: https://yameogo123-backend.hf.space/docs
### Lien APPLICATION: https://yameogo123-frontend.hf.space

## Accessibilité 2:
### cloner le github et appliquer la commande docker compose up (--build)


Réalisation d'une plateforme de prediction de fleurs iris d'une part et de prédiction de cas de diabète ou non.
Ces prédictions sont: 
- soit fait de façon ponctuelle avec un formulaire pour chaque cas ou plutôt 
- soit par batch avec une base de données à téléverser
Les résultats retournés sont la prédiction de la classe et sa probabilité de prédiction.

Pour se faire, notre travail a été scindé en frontend avec streamlit, backend avec FastAPI.
Ils ont tous les deux été hébergés sur hugging face et accessible via les liens données plus haut.


# CLIENT

realiser avec streamlit, il contient trois pages. 
- Une première page montrant le contenu de données diabete et iris: <br/>
- Une seconde page donnant la possibilité, grâce à un formulaire de prédire un type d'iris d'une part et une détection de diabete de l'autre. <br/>
- Une troisième page faisant des prédictions par lots (fichier) de données. <br/>
NB: Source de données: (https://github.com/plotly/datasets/tree/master)


# SERVER 

realiser avec fastapi il contient: 
- d'abord une url de recuperation de données de diabete et iris.
- elle contient les modèles qui ont été entrainé sur iris, diabète avec la regression logistique (voir train.ipynb)
- enfin elle contient les endpoint nous permettant de faire les predictions sur les données reçu de notre CLIENT

