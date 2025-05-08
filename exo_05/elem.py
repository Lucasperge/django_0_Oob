class Elem:
    def __init__(self, content, tag_name, is_self_closing=False):
        """Initialise l'élément HTML avec son contenu, son nom de balise et si c'est une balise auto-fermant."""
        self.tag_name = tag_name  # Le nom de la balise HTML
        self.content = content    # Le contenu de l'élément (peut être une chaîne ou une liste)
        self.is_self_closing = is_self_closing  # Si la balise est auto-fermant (comme <img />)
        
    def __str__(self):
        """Retourne la représentation HTML de l'élément."""
        if isinstance(self.content, list):
            content_str = ''.join(str(item) for item in self.content)  # Si le contenu est une liste, on les transforme en chaînes
        else:
            content_str = self.content  # Sinon c'est simplement une chaîne

        if self.is_self_closing:
            return f"<{self.tag_name} {content_str} />"  # Balise auto-fermant
        else:
            return f"<{self.tag_name}>{content_str}</{self.tag_name}>"  # Balise normale

    def add_content(self, new_content):
        """Ajoute du contenu à l'élément."""
        if isinstance(self.content, list):
            self.content.append(new_content)  # Ajoute un élément à la liste
        else:
            self.content += new_content  # Ajoute directement une chaîne de caractères au contenu

# Classes spécifiques héritant de Elem

class Html(Elem):
    def __init__(self, content):
        super().__init__(content, 'html')

class Head(Elem):
    def __init__(self, content):
        super().__init__(content, 'head')

class Body(Elem):
    def __init__(self, content):
        super().__init__(content, 'body')

class Title(Elem):
    def __init__(self, content):
        super().__init__(content, 'title')

class Meta(Elem):
    def __init__(self, content=""):
        # Meta est une balise auto-fermant, donc pas de contenu, juste des attributs
        super().__init__(content, 'meta', is_self_closing=True)

class Img(Elem):
    def __init__(self, src):
        # L'élément <img> a un attribut 'src', donc il est auto-fermant
        super().__init__(f'src="{src}"', 'img', is_self_closing=True)

class Table(Elem):
    def __init__(self, content):
        super().__init__(content, 'table')

class Th(Elem):
    def __init__(self, content):
        super().__init__(content, 'th')

class Tr(Elem):
    def __init__(self, content):
        super().__init__(content, 'tr')

class Td(Elem):
    def __init__(self, content):
        super().__init__(content, 'td')

class Ul(Elem):
    def __init__(self, content):
        super().__init__(content, 'ul')

class Ol(Elem):
    def __init__(self, content):
        super().__init__(content, 'ol')

class Li(Elem):
    def __init__(self, content):
        super().__init__(content, 'li')

class H1(Elem):
    def __init__(self, content):
        super().__init__(content, 'h1')

class H2(Elem):
    def __init__(self, content):
        super().__init__(content, 'h2')

class P(Elem):
    def __init__(self, content):
        super().__init__(content, 'p')

class Div(Elem):
    def __init__(self, content):
        super().__init__(content, 'div')

class Span(Elem):
    def __init__(self, content):
        super().__init__(content, 'span')

class Hr(Elem):
    def __init__(self):
        super().__init__("", 'hr', is_self_closing=True)

class Br(Elem):
    def __init__(self):
        super().__init__("", 'br', is_self_closing=True)
