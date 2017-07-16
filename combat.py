import time


def attack_enemy(glad1, glad2):
    print "----------"
    print "%s attacks for %s damage!" % (glad1.name, glad1.damage)
    glad2.hp -= glad1.damage
    print "%s Hp: %s" % (glad2.name, glad2.hp)

def attack_me(glad1, glad2):
    print "----------"
    print "%s attacks for %s damage!" %(glad2.name, glad2.damage)
    glad1.hp -= glad2.damage
    print "%s Hp: %s" %(glad1.name, glad1.hp)

def fight(glad1, glad2):
    while True:
        attack_enemy(glad1, glad2)
        if glad2.hp <= 0:
            break
        else:
            time.sleep(1.3)
            attack_me(glad1, glad2)
            if glad1.hp <= 0:
                break
            else:
                time.sleep(1.3)

def battle(glad1, glad2):
    print "----------"
    print "--Fight!--"
    fight(glad1, glad2)
    if glad1.hp <=0:
        print "-------"
        print '%s Wins!' % glad2.name
        print "-------"
    elif glad2.hp <=0:
        print "-------"
        print '%s Wins!' % glad1.name
        glad1.exp += (glad2.level * 15)
        print "-------"

