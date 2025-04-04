class Base:
    def __init__(self, name, health, attack_power, defense, speed):
        self.name=name
        self.health=health
        self.attack_power=attack_power
        self.defense=defense
        self.speed=speed

    def attack(self, target):
        damage=max(1, self.attack_power-self.defense)

    def take_damage(self, amount):
        self.health-=amount
    
    def is_alive(self, health):
        return self.health>0
    
class Warrior(Base):
    def __init__(self, name):
        super().__inti__(name, health=150, attack_power=20, defense=25, speed=2)
        self.rage=0
    def take_damage(self, amount):
        return super().take_damage(amount)
        self.rage+=amount//2
        if self.health<30:
            attack_power*=2
        
class Mage(Base):
    def __inti__(self, name):
        super().__inti__(name, health=100, attack_power=40, defense=10, speed=2)
        self.mage=0
    def attack(self, target):
        return super().attack(target)
    
class Archer(Base):
    def __inti__(self, name):
        super().__init__(name, health=100, attack_power=30, defense=10, speed=10)
    
        