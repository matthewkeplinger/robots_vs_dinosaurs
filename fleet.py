#Name: Matt Keplinger
#Date: 11 Aug 2021
#File: fleet.py
#Proj: Robots vs. Dinosaurs

#imports
from robot import Robot

class Fleet:
    def __init__(self):
        self.robots_list = []
        self.create_fleet()

    def create_fleet(self):
        tank = Robot("Grunt", 100)
        scout = Robot("Recon", 80)
        sniper = Robot("Killshot", 80)

        self.robots_list.append(tank)
        self.robots_list.append(scout)
        self.robots_list.append(sniper)