from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.herd = []
        self.add_to_herd()

    def add_to_herd(self):
        self.herd.append(Dinosaur("T-Rex", 200, 80))
        self.herd.append(Dinosaur("Raptor", 100, 40))
        self.herd.append(Dinosaur("Pterodactyl",100, 50))

    # def add_to_herd(self):
    #     trex = Dinosaur("T-Rex", 200, 80)
    #     raptor = Dinosaur("Raptor", 100, 40)
    #     flyer = Dinosaur("Pterodactyl",100, 50)
    
    #     self.herd.append(trex)
    #     self.herd.append(raptor)
    #     self.herd.append(flyer)
