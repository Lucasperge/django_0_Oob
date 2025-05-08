import random

# Exception pour la machine cassée
class BrokenMachineException(Exception):
    def __init__(self):
        super().__init__("This coffee machine has to be repaired.")

# La classe qui représente la machine à café
class CoffeeMachine:
    def __init__(self):
        self.served_beverages = 0
        self.is_broken = False
        self.empty_cup_count = 0

    def repair(self):
        if self.is_broken:
            self.is_broken = False
            self.served_beverages = 0
            self.empty_cup_count = 0
            print("The coffee machine has been repaired.")
        else:
            print("The machine is already working.")

    def serve(self, beverage):
        if self.is_broken:
            raise BrokenMachineException()

        self.served_beverages += 1

        # Vérifier si la machine doit tomber en panne après 10 boissons
        if self.served_beverages > 10:
            self.is_broken = True
            raise BrokenMachineException()

        # Distribution des boissons et des tasses vides
        if random.random() < 0.8:  # 80% de chance de servir une vraie boisson
            self.empty_cup_count = 0  # Réinitialiser le compteur de tasses vides
            return beverage()
        else:
            self.empty_cup_count += 1
            # Si trop de tasses vides consécutives, servir une vraie boisson
            if self.empty_cup_count > 3:
                self.empty_cup_count = 0  # Réinitialiser le compteur
                return beverage()
            return EmptyCup()

# Classe représentant une tasse vide
class EmptyCup:
    def __init__(self):
        self.name = "empty cup"
        self.price = 0.90

    def description(self):
        return "An empty cup?! Gimme my money back!"

    def __str__(self):
        return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}"

# Importer les boissons du fichier beverages.py
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

import random
import time  # Importer la fonction time

if __name__ == "__main__":
    # Instancier la machine à café
    coffee_machine = CoffeeMachine()

    # Créer des instances des boissons
    beverages = [Coffee, Tea, Chocolate, Cappuccino]

    # Tester jusqu'à ce que la machine tombe en panne, puis la réparer et recommencer
    while True:
        try:
            # Choisir une boisson aléatoire parmi les disponibles
            beverage_class = random.choice(beverages)
            beverage = coffee_machine.serve(beverage_class)
            print(beverage)
            time.sleep(1)  # Attendre 1 seconde avant d'afficher la prochaine boisson
        except BrokenMachineException:
            print("This coffee machine has to be repaired.")
            coffee_machine.repair()
            time.sleep(1)  # Attendre 1 seconde après la réparation
