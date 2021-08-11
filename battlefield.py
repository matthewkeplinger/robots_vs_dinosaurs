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
        #REMOVE BEFORE SUBMISSION: MATT, THESE ARE YOUR NOTES ONLY
        #Step 1: make sure each list has at least 1 object left (one fighter) (WHILE LOOP)
         # IF not, side with 0 loses (if/elif and call method display_winners())
        #Step 2: Prompt user to see who attacks first (input() and if/elif with appropriate _turn() method)
        #Step 3: When that turn is finished, immediately launch next (dino then robot for example)
        #must re-evaluate every single iteration of if/elif

        while len(self.herd.dinosaur_list) > 0 and  len(self.fleet.robots_list) > 0:
            battle_choice = input("Who is attacking: dinosaurs or robots? ")

            if(battle_choice == 'dinosaurs'):
                Battlefield.dino_turn(self)
            elif(battle_choice == 'robots'):
                Battlefield.robo_turn(self)

    #Dinosaur Turn, need to clean up these methods
    def dino_turn(self):
        #REMOVE BEFORE SUBMISSION: MATT, THESE ARE YOUR NOTES ONLY
        #STEP 1: have dinosaur at index 0 attack robot at index 0; print output to show user that attack happened
        #STEP 2: Display remaining health of robot
        #STEP 3: Check to see if robot is dead.  if so, remove from list and continue battle
        self.herd.dinosaur_list[0].attack(self.fleet.robots_list[0])
        print(self.herd.dinosaur_list[0].name + " attacked " + self.fleet.robots_list[0].name + " for " + str(self.herd.dinosaur_list[0].attack_power) + " damage!")
        print(self.fleet.robots_list[0].name + " has " + str(self.fleet.robots_list[0].health) + " health remaining.")

        if(self.fleet.robots_list[0].health <= 0):
            print(self.fleet.robots_list[0].name + " got the blue screen of death!\n")
            self.fleet.robots_list.pop(0)

    #Robot Turn, need to come back and clean this up: Just copy and modify the dino loop and get rid of mess
    def robo_turn(self):
        self.fleet.robots_list[0].attack(self.herd.dinosaur_list[0])
        print(self.fleet.robots_list[0].name + " attacked " + self.herd.dinosaur_list[0].name + " for " + str(self.fleet.robots_list[0].weapon.attack_power) + " damage!")
        print(self.herd.dinosaur_list[0].name + " has " + str(self.herd.dinosaur_list[0].health) + " health remaining.")
        
        if(self.herd.dinosaur_list[0].health <= 0):
            print(self.herd.dinosaur_list[0].name + " is extinct!\n")
            self.herd.dinosaur_list.pop(0)

    #Figure out how to list opponents and choose from remaining opponents
    def show_dino_opponent_options(self):
        pass
    def show_robo_opponent_options(self):
        pass

    # Display a winner of the Robot vs. Dinosaur battles
    def display_winners(self, victor):
        print("And the " + victor + " are victorious!")
        
