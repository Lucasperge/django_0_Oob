from elem import Elem, Text

class Html(Elem):
    def __init__(self, content):
        super().__init__('html', content)

class Head(Elem):
    def __init__(self, content):
        super().__init__('head', content)

class Body(Elem):
    def __init__(self, content):
        super().__init__('body', content)

class Title(Elem):
    def __init__(self, content):
        super().__init__('title', [Text(content)])

class H1(Elem):
    def __init__(self, content):
        super().__init__('h1', [Text(content)])

class P(Elem):
    def __init__(self, content):
        super().__init__('p', [Text(content)])

class Img(Elem):
    def __init__(self, src):
        super().__init__('img', is_empty=True)
        self.attributes = {'src': src}
