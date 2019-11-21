class Item:
    gold = 1
    def __init__(self, name, gold):
        self.name = name
        self.gold = gold

    def display(self):
        print("Name: " + self.name)
        print("Sell Value: " + str(self.gold))

class Sword(Item):
    damage = 0
    def __init__(self, damage):
        super().__init__("Sword", 1)
        self.damage = damage

    def display(self):
        super().display()
        print("Damage: " + str(self.damage))

class Gem(Item):
    def __init__(self):
        super().__init__("Gem", 10)

class Armour(Item):
    protection = 0
    def __init__(self, protection):
        super().__init__("Armour", 5)
        self.protection = protection

    def display(self):
        super().display()
        print("Protection: " + str(self.protection))

inventory = [ Sword(3), Armour(4), Gem(), Item("VendorTrash", 2) ]

for item in inventory:
    item.display()
    print("-----")