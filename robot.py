#Name: Matt Keplinger
#Date: 11 Aug 2021
#File: robot.py
#Proj: Robots vs. Dinosaurs

#imports
from weapon import Weapon
from dinosaur import Dinosaur

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = Weapon("Pulse Rifle", 50)

    def robot_specs(self):
        print("\nRobot Name:   ", self.name)
        print("Robot Health: ", self.health)
        print("Robot Weapon: ", self.weapon.name)
        print("Attack Power: ",self.weapon.attack_power)

    def robot_attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power


    # def assign_weapon(self,Weapon):
    #     # sword = Weapon("Energy Sword", 50)
    #     pulse_rifle = Weapon("Pulse Rifle", 40)
    #     # gauss_rifle = Weapon("Gauss Rifle", 100)
    #     self.weapon = pulse_rifle