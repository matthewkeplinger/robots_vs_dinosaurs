from robot import Robot

class Dinosaur:
    def __init__(self,name,health, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        
    def dino_specs(self):
        print("\nDinosaur Name:   ", self.name)
        print("Dinosaur Health: ", self.health)
        print("Dinosaur AttPWR: ", self.attack_power)

    def dino_attack(self, robot):
        robot.health -= self.attack_power
        print(self.name + " attacked for " + self.attack_power + "damage")


  