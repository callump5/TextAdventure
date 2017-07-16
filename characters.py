class gladiator(object):
    def __init__(self, name):
        self.name = name
        self.exp = 1000
        self.level = 1
        self.inventory = []
        self.equipedItems = []
        self.base_hp = 180
        self.hp = 0
        self.base_damage = 24
        self.damage = 0

    def update_level(self):
        self.level = self.exp / 150

    def update_damage_stat(self):
        self.update_level()
        items_damage = 0
        for items in self.equipedItems:
            items_damage += items.damage

        self.damage = items_damage + self.base_damage + self.level

    def update_hp_stat(self):
        self.update_level()
        items_hp = 0
        for items in self.equipedItems:
            items_hp += items.hp

        self.hp = items_hp + self.base_hp + self.level

    def update_stats(self):
        self.update_damage_stat()
        self.update_hp_stat()
        self.update_level()

    def stats(self):
        self.update_stats()
        print "---" + self.name + "---"
        print "---"
        print "Hp: %s" % self.hp
        print "---"
        print "Damage: %s" %self.damage
        print "---"
        print "Level: %s" % self.level
        print "Exp: %s" % self.exp
        print "Equipment:"
        for items in self.equipedItems:
            print "--"
            print "%s: " %items.name
            print "-"
            print "Dam: %s" % items.damage
            print "Hp: %s" % items.hp
            print "--"
        print "------"
        print "------"


c = gladiator(raw_input("Enter Name: "))

e = gladiator('Gladitator')
