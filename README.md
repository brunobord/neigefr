## NEIGEFR

This is a #uksnow ripoff. But for french people. So this README is written in
French.

-------------------------------------------------------------------------------

Bon, alors. Depuis quelques années on a droit à un hashtag sur la toile, que
je vois avec envie dans ma timeline:

    #uksnow

Et ça m'énerve que les poudingues aient un hashtag à eux qui leur permette de
voir la [carte de l'enneigement en quasi-direct](http://uksnowmap.com/).

Alors j'ai pris mon courage et mon [Django](http://djangoproject.com) à deux
mains et voilà.

### Comment ça marche ?

N'importe quel twittos, dès qu'il voit des machins blancs tomber du ciel,
l'hiver, peut twitter comme suit :

    LOL il neige #neigefr 75008 3/10 MDR

Les éléments indispensables sont :

* "#neigefr" : c'est le hashtag **OFFICIEL**
* "75008": c'est le code postal de l'endroit où tombe la neige.

De manière optionnelle, tu peux ajouter un "niveau" sur 10 qui indique à quel
point il est en train de neiger. A titre indicatif :

* *7/10* ou plus - Tempête de neige !
* *5/10* ou *6/10* - Solide averse
* *3/10* ou *4/10* - Petite averse
* *1/10* ou *2/10* - Quelques flocons
* *0/10* - Y'a plus la neige... :-(

Avec un peu de chances, ton tweet viendra enrichir la carte de l'enneigement en
France sur [Neige FR](http://neigefr.org).


### A quel point c'est précis ?

Tout dépend de toi. De toi, de tes amis, et de ta propension à twitter dès qu'il
neige. Plus nous serons nombreux à twitter en utilisant le hashtag `#neigefr`,
plus la carte représentera en quasi-direct les chutes de neige sur le
territoire.


### Installation

Pour faire tourner le code:

    git clone git@github.com:brunobord/neigefr.git
    cd neigefr
    virtualenv --distribute .venv
    source .venv/bin/activate
    pip install -r requirements.txt


### Configuration

Créez un fichier ``neigefr/settings.py`` et ajoutez-y le minimum:

    from .default_settings import *  # noqua

    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    INTERNAL_IPS = ('127.0.0.1',)

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'neigefr.db',
        }
    }

    SECRET_KEY = 'something secret'

    # For development, don't do cache-busting
    STATICFILES_STORAGE = ('django.contrib.staticfiles.storage.'
                           'StaticFilesStorage')

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )


### Références

* J'ai "piqué" quelques lignes de code issues de [https://github.com/bruntonspall/uksnow](https://github.com/bruntonspall/uksnow), le code de `#uksnow`
* Tu peux suivre [@_neigefr](http://twitter.com/_neigefr) sur Twitter, mais ne t'attends pas à un déluge de tweets,
* L'icône utilisée provient du [Noun project](http://thenounproject.com/noun/snow/#icon-No64), et appartient au domaine public,
* Elle a été tripatouillée par  [JazzyNico](https://twitter.com/JazzyNico) pour la tricoloriser et la rendre légèrement cocardière sur les bords,
* J'utilise le framework ["Twitter Bootstrap"](http://twitter.github.com/bootstrap/) pour le layout HTML5/CSS. J'espère que votre mobile apprécie,
* Les cartes sont propulsées par [OpenStreetMap](http://www.openstreetmap.org/) et [CloudMade](http://maps.cloudmade.com/) et utilisent l'API Javascript [Leaflet](http://leaflet.cloudmade.com/),
* Les tuiles sont fournies par [Thunderforest](http://thunderforest.com/)
* La police du titre est ["Bubblegum Sans"](http://www.google.com/webfonts/specimen/Bubblegum+Sans),
* La géolocalisation (coordination code postal -> coordonnées GPS) utilise le projet [Geocoders](https://github.com/simonw/geocoders), de Simon Willison,
* On récupère les tweets via [requests](https://github.com/kennethreitz/requests), de Kenneth Reitz

### Licence d'utilisation

Le code de cette application Django peut être réutilisé par n'importe qui, pour
en faire n'importe quoi. Voilà pourquoi j'ai décidé d'élever ce code dans le
**Domaine Public** (aussi appelé CC0).
