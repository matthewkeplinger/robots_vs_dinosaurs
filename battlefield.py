# Name: Matt Keplinger
# Date: 11 Aug 2021
#File: battlefield.py
# Proj: Robots vs. Dinosaurs

# imports
#from robot import Robot
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
        print("**************************************")
        print("ROBOTS VS. DINOSAURS")
        print("**************************************")
        print("A battle of the future vs. the past")
        print("iRobot vs. Jurassic Park")
        print("Let's Get ready to RUUUUMMMMBLE")
        print("**************************************")

    def battle(self):
        self.dino_turn()
        self.robo_turn()

    def dino_turn(self):
        for dinosaur in self.herd.dinosaur_list:
            if(dinosaur.health == 0):
                print(dinosaur.name + "is out of the fight.")
                self.herd.dinosaur_list.remove(dinosaur)

            if(len(self.herd.dinosaur_list) == 0):
                self.display_winners("Robots")

        robot = 0
        print("And the Dinosaurs Attack!")
        for dino in self.herd.dinosaur_list:
            if (dino.health > 0):

                dino.dino_attack(self.fleet.robots_list[robot])
                print(self.fleet.robots_list[robot].name + " has " + (str(self.fleet.robots_list[robot].health) + " health remaining"))
            while robot < len(self.fleet.robots_list):
                robot += 1
        dinosaur.dino_attack()

    def robo_turn(self):
        for robot in self.fleet.robots_list:
            if(robot.health == 0):
                print(robot.name + "is out of the fight.")
                self.fleet.robot_list.remove(robot)

            if(len(self.fleet.robots_list) == 0):
                self.display_winners("Dinosaurs")

        dinosaur = 0
        for robot in self.fleet.robots_list:
            if (robot.health > 0):
                print("And the Robots Attack!")
                robot.robot_attack(self.herd.dinosaur_list[dinosaur])
                print(self.herd.dinosaur_list[dinosaur].name + " has " + (str(self.herd.dinosaur_list[dinosaur].health) + " health remaining"))
            while dinosaur < len(self.herd.dinosaurs_list):
                dinosaur += 1
        robot.robot_attack()

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self, victor):
        print("And the " + victor + " are victorious!")
        
