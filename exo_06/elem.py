class Elem:
    def __init__(self, name, content=None, is_empty=False):
        self.name = name
        self.content = content if content is not None else []
        self.is_empty = is_empty
        self.attributes = {}  # Toujours un dictionnaire vide par défaut pour les attributs

    def __str__(self):
        # Si l'élément est de type "text", retourne juste son contenu
        if isinstance(self, Text):
            return self.content[0]

        # Si l'élément est vide (comme <img>), on traite cela différemment
        if self.is_empty:
            return f"<{self.name} {self._get_attributes()}/>"
        else:
            # On convertit chaque élément de content en une chaîne de caractères
            content_str = "".join([str(item) for item in self.content])
            return f"<{self.name} {self._get_attributes()}>{content_str}</{self.name}>"

    def _get_attributes(self):
        # Si self.attributes est vide, retourner une chaîne vide
        return " ".join(f'{key}="{value}"' for key, value in self.attributes.items())

class Text(Elem):
    def __init__(self, content):
        # Les Text n'ont pas d'attributs, juste une chaîne de contenu
        super().__init__('text', [content], True)
