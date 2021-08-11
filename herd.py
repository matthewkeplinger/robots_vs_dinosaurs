#Name: Matt Keplinger
#Date: 11 Aug 2021
#File: herd.py
#Proj: Robots vs. Dinosaurs

#imports
from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaur_list = []
        self.create_herd()

    # def create_herd(self):
    #     self.dinosaur_list.append(Dinosaur("T-Rex", 200, 80))
    #     self.dinosaur_list.append(Dinosaur("Raptor", 100, 40))
    #     self.dinosaur_list.append(Dinosaur("Pterodactyl",100, 50))

    def create_herd(self):
        trex = Dinosaur("T-Rex", 200, 80)
        raptor = Dinosaur("Raptor", 100, 40)
        flyer = Dinosaur("Pterodactyl",100, 50)

        self.dinosaur_list.append(trex)
        self.dinosaur_list.append(raptor)
        self.dinosaur_list.append(flyer)
