from random  import randint
from Team import *

printActionDescription = True

def dprint(s):
    if printActionDescription:
        print(s)

#Constants for Mage Type        
manaCost = 20
manaRecovery = 30


class Character(object):
    def __init__(self):
        self.name = ''
        self.maxhp = 1000
        self.hp = 1000
        self.str = 0
        self.maxmana = 0
        self.mana = 0
        self.cost = 9999999999
        self.alive = True

    def act(self,myTeam,enemy):
        return

    def gotHurt(self,damage):
        if damage >= self.hp:
            self.hp = 0
            self.alive = False
            dprint(self.name + ' died!')
        else:
            self.hp -= damage
            dprint(self.name +
                   f' hurt with remaining hp {self.hp}.')

    

class Fighter(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Fighter'
        self.maxhp = 1200
        self.hp = 1200
        self.str = 100
        self.cost = 100

    def act(self,myTeam,enemy):
        target = randAlive(enemy)
        dprint(f'Hurt enemy {target} by damage {self.str}.')
        enemy[target].gotHurt(self.str)
  

class Mage(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Mage'
        self.maxmana = 50
        self.mana = 50
        self.maxhp = 800
        self.hp = 800
        self.cost = 200
        self.int = 400

    def cast(self,myTeam,enemy):
        self.mana -= manaCost
        target = randAlive(enemy)
        dprint(f'Strike enemy {target} with spell')
        enemy[target].gotHurt(self.int)
        
    def act(self,myTeam,enemy):
        if self.mana < manaCost:
            self.mana += manaRecovery
            dprint(f'Mana recover to {self.mana}.')
        else:
            self.cast(myTeam,enemy)

class Berserker(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Berserker'
        self.cost = 200
        
    def act(self, myTeam, enemy):
        if self.hp >= self.maxhp / 2:
            target = randAlive(enemy)
            dprint(f'Hurt enemy {target} by damage {self.str}.')
            enemy[target].gotHurt(self.str)
        else:
            self.str *= 2
            target = randAlive(enemy)
            dprint("Berserk mode! Attack double!")
            dprint(f'Hurt enemy {target} by damage {self.str}.')
            enemy[target].gotHurt(self.str)
            

class ArchMage(Character):
    def __init__(self):
        super().__init__()
        self.name = 'ArchMage'
        self.cost = 600
    
    def cast(self,myTeam,enemy):
        self.mana -= manaCost
        if len(myTeam) == 1:
            dprint('Cast KABOOOOOOM ! (Damage 800) to every enemy!')
            for i in len(enemy):
                enemy[i].gotHurt(800)
                
class Necromancer(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Necromancer'
        self.cost = 400
        
    def cast(self, myTeam, enemy):
        self.mana -= manaCost
        target = randDeath(myTeam)
        if target == 1:
            myTeam[target] = Fighter()
        if target == 2:
            myTeam[target] = Mage()
        if target == 3:
            myTeam[target] = Berserker()
        if target == 4:
            myTeam[target] = ArchMage()
        if target == 5:
            myTeam[target] = Necromancer()
        
        myTeam[target].hp /= 2
        dprint(f'Reving member {target} with hp {myTeam[target].hp}! ')

