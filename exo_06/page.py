from elements import Html, Head, Body, Title, H1, P, Img
from elem import Elem

class Page:
    def __init__(self, root_element):
        self.root_element = root_element

    def is_valid(self):
        # Si l'élément racine n'est pas un Html, on retourne False
        if not isinstance(self.root_element, Html):
            return False

        head = None
        body = None

        # On parcourt les éléments du document pour vérifier qu'il y a bien une tête et un corps
        for elem in self.root_element.content:
            if isinstance(elem, Head):
                if head is not None:  # On vérifie qu'il y a un seul Head
                    return False
                head = elem
            elif isinstance(elem, Body):
                if body is not None:  # On vérifie qu'il y a un seul Body
                    return False
                body = elem

        # Vérifie qu'il y a bien un seul Title dans Head
        if head:
            title_count = sum(1 for item in head.content if isinstance(item, Title))
            if title_count != 1:
                return False

        # Vérifie que Body ne contient que des éléments valides
        if body:
            for elem in body.content:
                if not isinstance(elem, (H1, P, Img)):
                    return False

        return True

    def __str__(self):
        return str(self.root_element)

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self))

# Code de test dans le même fichier (fin du fichier)
if __name__ == "__main__":
    # Création d'une page HTML avec un titre, une image et un en-tête
    title = Title("Hello ground!")
    head = Head([title])
    body = Body([H1("Oh no, not again!"), Img("http://i.imgur.com/pfp3T.jpg")])

    # Création de l'élément racine HTML
    html = Html([head, body])

    # Création de la page
    page = Page(html)

    # Vérification de la validité de la page
    print("La page est-elle valide ? ", page.is_valid())

    # Affichage du code HTML
    print(str(page))

    # Écriture dans un fichier HTML
    page.write_to_file("output.html")
