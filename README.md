## NEIGEFR

This is a #uksnow ripoff. But for french people. So this README is written in
French.

Bon, alors. Depuis quelques années on a droit à un hashtag sur la toile, que
je vois avec envie dans ma timeline:

    #uksnow

Et ça m'énerve que les poudingues aient un hashtag à eux qui leur permette de
voir la [carte de l'enneigement en quasi-direct](http://uksnowmap.com/).

Alors j'ai pris mon courage et mon [Django](http://djangoproject.com) à deux
mains et voilà.

### Comment ça marche ?

N'importe quel twittos, dès qu'il voit des machins blancs tomber du ciel,
l'hiver, il peut twitter comme suit :

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

### Références

* J'ai "piqué" quelques lignes de code issues de [https://github.com/bruntonspall/uksnow](https://github.com/bruntonspall/uksnow), le code de `#uksnow`
* Tu peux suivre [@_neigefr](http://twitter.com/_neigefr) sur Twitter, mais ne t'attends pas à un déluge de tweets.
* L'icône utilisée provient du [Noun project](http://thenounproject.com/noun/snow/#icon-No64), et appartient au domaine public.
