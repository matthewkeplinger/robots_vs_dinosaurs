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

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
