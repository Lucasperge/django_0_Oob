

class Intern:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.name = name

    def __str__(self):
        return self.name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return self.Coffee()

if __name__ == "__main__":
    # Créer deux stagiaires
    intern1 = Intern()
    intern2 = Intern("Mark")

    # Afficher leur nom
    print(intern1)
    print(intern2)

    # Demander à Mark de faire un café
    coffee = intern2.make_coffee()
    print(coffee)

    # Demander à l'autre de travailler (et attraper l'erreur)
    try:
        intern1.work()
    except Exception as e:
        print(e)



