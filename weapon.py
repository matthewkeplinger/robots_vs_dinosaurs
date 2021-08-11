#Name: Matt Keplinger
#Date: 11 Aug 2021
#File: weapon.py
#Proj: Robots vs. Dinosaurs

#imports
class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        
    def weapon_specs(self):
        print("\nWeapon Name: ", self.name)
        print("Attack Power: ", self.attack_power)
