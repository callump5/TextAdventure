class item(object):
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def equip(self, glad):
        glad.equipedItems.append(self)
        glad.update_stats()

    def unequip(self, glad):
        glad.equipedItems.remove(self)
        glad.update_stats()

    def add_to_inv(self, glad):
        glad.inventory.append(self)
        glad.update_stats()

    def remove_from_inv(self, glad):
        glad.inventory.remove(self)
        glad.update_stats()


dagger = item("Dagger", 190, 12)
gladius = item ("Gladius", 100, 25)

weapons = [dagger, gladius]