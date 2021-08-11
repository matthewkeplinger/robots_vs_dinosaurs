#Name: Matt Keplinger
#Date: 11 Aug 2021
#File: battlefield.py
#Proj: Robots vs. Dinosaurs

#imports
from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()

    def display_welcome(self):
        print("\nROBOTS VS. DINOSAURS")
        print("\n A battle of the future vs. the past")
        print("\n iRobot vs. Jurassic Park")
        print("\nLet's Get ready to RUUUUMMMMBLE")

    def battle(self):
        print("")
        pass
    
    def dino_turn(self, robot, dinosaur):
        print("Team Dinosaur on the attack")
        dinosaur.dino_attack()
        pass

    def robo_turn(self, robot, dinosaur):
        print("Team Robot on the attack")
        robot.robot_attack()
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        print("And the winner is: ")
        pass