def beverages():
    class HotBeverage:
        def __init__(self):
            self.price = 0.30
            self.name = "hot beverage"

        def description(self):
            return "Just some hot water in a cup."

        def __str__(self):
            return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}"

    class Coffee(HotBeverage):
        def __init__(self):
            super().__init__()  # Appel au constructeur de la classe parente (HotBeverage)
            self.price = 0.40
            self.name = "coffee"

        def description(self):
            return "A coffee, to stay awake."

    class Tea(HotBeverage):
        def __init__(self):
            super().__init__()
            self.price = 0.30
            self.name = "tea"

        def description(self):
            return "Just some hot water in a cup."

    class Chocolate(HotBeverage):
        def __init__(self):
            super().__init__()
            self.price = 0.50
            self.name = "chocolate"

        def description(self):
            return "Chocolate, sweet chocolate..."

    class Cappuccino(HotBeverage):
        def __init__(self):
            super().__init__()
            self.price = 0.45
            self.name = "cappuccino"

        def description(self):
            return "Un po’ di Italia nella sua tazza!"

    # Créer des instances de chaque boisson
    hot_beverage = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()

    # Afficher les informations de chaque boisson
    print(hot_beverage)
    print(coffee)
    print(tea)
    print(chocolate)
    print(cappuccino)

# Cette partie ne sera exécutée que si on lance le fichier directement
if __name__ == "__main__":
    beverages()  # Appeler la fonction beverages() pour exécuter tout le code
