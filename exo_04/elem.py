class Elem:
    """Classe pour représenter un élément HTML."""

    class ValidationError(Exception):
        """Exception personnalisée pour contenu invalide."""
        pass

    def __init__(self, tag, attributes=None, content=None, elem_type='double'):
        # Nom de la balise HTML, ex: 'p', 'img'
        self.tag = tag
        # Dictionnaire des attributs HTML, ex: {'src': 'image.jpg'}
        self.attributes = attributes if attributes else {}
        # Liste de contenu HTML (texte ou autres balises)
        self.content = []
        # Type : soit 'double' (avec balise ouvrante et fermante), soit 'self-closing'
        self.elem_type = elem_type
        # Ajoute le contenu initial s’il y en a
        if content:
            self.add_content(content)

    def __str__(self):
        # Gère les attributs HTML sous forme de string
        attrs = ''.join(f' {k}="{v}"' for k, v in self.attributes.items())

        # Balise auto-fermante
        if self.elem_type == 'self-closing':
            return f"<{self.tag}{attrs} />"

        # Balise normale avec contenu
        content_str = ''
        for c in self.content:
            content_str += str(c) + '\n'
        return f"<{self.tag}{attrs}>\n{content_str.strip()}\n</{self.tag}>"

    def add_content(self, new_content):
        # Vérifie que le contenu est soit une liste, soit un élément, soit une string
        if isinstance(new_content, list):
            for c in new_content:
                if not isinstance(c, (Elem, str)):
                    raise Elem.ValidationError("Invalid content type")
                self.content.append(c)
        else:
            if not isinstance(new_content, (Elem, str)):
                raise Elem.ValidationError("Invalid content type")
            self.content.append(new_content)


# Partie test : création d'une page HTML simple
if __name__ == "__main__":
    # Crée un titre <h1>"Oh no, not again!"</h1>
    h1 = Elem("h1", content='"Oh no, not again!"')

    # Crée une image <img src="..."/>
    img = Elem("img", attributes={"src": "http://i.imgur.com/pfp3T.jpg"}, elem_type="self-closing")

    # Crée le corps <body>...</body>
    body = Elem("body")
    body.add_content(h1)
    body.add_content(img)

    # Crée le titre de l'onglet <title>"Hello ground!"</title>
    title = Elem("title", content='"Hello ground!"')

    # Crée le <head> contenant le <title>
    head = Elem("head")
    head.add_content(title)

    # Assemble tout dans la balise <html>
    html = Elem("html")
    html.add_content(head)
    html.add_content(body)

    # Affiche le code HTML complet
    print(html)


