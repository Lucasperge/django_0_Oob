from elem import Html, Head, Body, Title, Meta, Img, H1

# Création d'une page HTML simple avec les classes que nous avons définies

# Créer le titre
title = Title('"Hello ground!"')

# Créer une image
img = Img('http://i.imgur.com/pfp3T.jpg')

# Créer un élément h1
h1 = H1('"Oh no, not again!"')

# Créer une structure HTML
html = Html([Head([title]), Body([h1, img])])

# Affichage du résultat
print(html)
