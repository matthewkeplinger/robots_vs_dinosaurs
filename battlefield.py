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

    # 1995-esque Intro
    def display_welcome(self):
        print("**************************************")
        print("ROBOTS VS. DINOSAURS")
        print("**************************************")
        print("A battle of the future vs. the past")
        print("iRobot vs. Jurassic Park")
        print("Let's Get ready to RUUUUMMMMBLE")
        print("**************************************")

    # Initiate battle 
    def battle(self):
        #Step 1: make sure each list has at least 1 object left (one fighter) (WHILE LOOP)
         # IF not, side with 0 loses (if/elif and call method display_winners())
        #Step 2: Prompt user to see who attacks first (input() and if/elif with appropriate _turn() method)
        #Step 3: When that turn is finished, immediately launch next (dino then robot for example)
        #must re-evaluate every single iteration of if/elif

        while len(self.fleet.robots_list) > 0 and len(self.herd.dinosaur_list) > 0:
            battle_choice = input("Who strikes first Blood (or Oil): dinosaurs or robots? ")

            if(battle_choice == 'dinosaurs'):
                Battlefield.dino_turn(self)
                if len(self.fleet.robots_list) > 0 and len(self.herd.dinosaur_list) > 0:
                    Battlefield.robo_turn(self)
                    #self.robo_turn
            elif(battle_choice == 'robots'):
                Battlefield.robo_turn(self)
                if len(self.fleet.robots_list) > 0 and len(self.herd.dinosaur_list) > 0:
                    Battlefield.dino_turn(self)
                    #self.robo_turn


    # Dinosaur Turn, need to clean up these methods
    def dino_turn(self):
        for dinosaur in self.herd.dinosaur_list:
            if(dinosaur.health == 0):
                print(dinosaur.name + "is out of the fight.")
                self.herd.dinosaur_list.remove(dinosaur)

            if(len(self.herd.dinosaur_list) == 0):
                self.display_winners("Robots")

        robot = 0
        print("And the Dinosaurs Attack!")
        for dinosaur in self.herd.dinosaur_list:
            if (dinosaur.health > 0):
                dinosaur.dino_attack(self.fleet.robots_list[0])
                print(self.fleet.robots_list[0].name + " has " + (str(self.fleet.robots_list[0].health) + " health remaining"))
            while robot < len(self.fleet.robots_list):
                robot += 1
        dinosaur.dino_attack(robot)

    #Robot Turn, need to come back and clean this up
    def robo_turn(self):
        for robot in self.fleet.robots_list:
            if(robot.health == 0):
                print(robot.name + "is out of the fight.")
                self.fleet.robots_list.remove(robot)

            if(len(self.fleet.robots_list) == 0):
                self.display_winners("Dinosaurs")

        dinosaur = 0
        for robot in self.fleet.robots_list:
            if (robot.health > 0):
                print("And the Robots Attack!")
                robot.robot_attack(self.herd.dinosaur_list[0])
                print(self.herd.dinosaur_list[0].name + " has " + (str(self.herd.dinosaur_list[0].health) + " health remaining"))
            while dinosaur < len(self.herd.dinosaur_list):
                dinosaur += 1
        robot.robot_attack(dinosaur)

    #determine what to do with this
    def show_dino_opponent_options(self):
        pass
    #determine what to do with this
    def show_robo_opponent_options(self):
        pass

    # Display a winner of the Robot vs. Dinosaur battles
    def display_winners(self, victor):
        print("And the " + victor + " are victorious!")
        
