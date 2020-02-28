Documentation
==================
## Introduction

Ce programme intéragit avec l'API Open Food Facts afin de permettre aux utilisateurs de récupérer un aliment et le comparer à la base de données de l'API et ainsi proposer à l'utilisateur, un substitut plus sain à l'aliment qui lui fait envie. Ce programme est créé avec le langage de programmation Python et utilise la base de données MySQL. 
Cette base de données permettra à l'utilisateur de posséder un compte et ainsi retrouver les aliments substitués qu'il aura lui-même enregistré. 

## Installation

_Utiliser SSH_ :

    git clone git@github.com:eme-subteno-it/project5.git

_Ou utiliser HTTPS_ :

    git clone https://github.com/eme-subteno-it/project5.git

_Pour l'ouvrir_ :

    python3 main.py

## Utilisation du programme

* **Assurez-vous d'avoir MySql d'installer en local.**

* **Connexion à MySQL**
    * Insérer votre identifiant MySQL
    * Insérer votre mot de passe MySQL

* **Création d'un compte** 
    * Taper 1 afin de créer un compte.
    * Remplissez le formulaire.
    * Appuyez sur "Entrée"

    _A la suite de ces informations, un script se lancera afin de vous créer un compte utilisateur mysql et d'y installer
    la base de données._

* **Connexion**
    * Remplissez le formulaire
    * Appuyez sur "Entrée"

* **Choisir une catégorie**
    * Taper le numéro situé devant la catégorie afin de l'a choisir et de voir apparaître ses produits.

* **Choisir un produit**
    * Taper également le numéro situé devant le produit afin de voir apparaître les informations de celui-ci ainsi que 
    son substitut.
    * Vous aurez ensuite le choix de le sauvegarder.

* **Visualiser vos aliments sauvegardés**
    * Un menu vous permet de visualiser les produits sauvegardés. Vous aurez alors la liste de tout vos produits 
    sauvegardé avec toutes leurs informations.

* **Mettre à jour les données**
    * Vous aurez la possibilité dans ce programme de mettre à jour les données. En acceptant, vous devez prendre conscience
    que ceci supprimera également vos produits substitués enregistrés.

* **Déconnexion**
    * La déconnexion s'effectuera lorsque vous quitterez le programme. En cliquant sur n'importe quelle touche non assignée.

Développement
=================
Le programme a été conçu en orienté objet, avec la classe **"Program"** qui est le "moteur" de celui-ci. Cette classe possède
toute les boucles nécessaires ainsi que certaines actions. Afin de récupérer toute les données (Catégories et produits), j'ai
utilisé l'API Open Food Facts. Pour l'insertion en base de données, j'ai utilisé un connecteur mysql compatible avec Python
et j'ai créé un script sql que vous pouvez retrouver dans le dossier /data permettant la création d'un utilisateur et d'une 
base de données. Ainsi, l'utilisateur aura besoin d'insérer ses identifiants MySQL qu'une seule fois, à l'inscription. Puis,
lors de la connexion au programme, l'utilisateur sera automatiquement connecté avec un identifiant SQL (présent dans le script sql).

L'utilisateur peut, s'il le souhaite, mettre à jour ses données. Pour ce faire, j'ai créé différentes requêtes SQL que vous
pouvez retrouver dans /models/Request.py qui DELETE (supprime) les valeurs présentes dans les tables afin de télécharger à
nouveau du contenu. L'utilisateur doit alors avoir conscience que s'il met à jour les données, il perdra ses produits substitués 
sauvegardés.

![](/data/img.png)