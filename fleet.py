from robot import Robot

class Fleet():
    def __init__(self):
        self.robots = []
        self.add_robots()

    def add_robots(self):
        self.robots.append(Robot("Grunt", 200))
        self.robots.append(Robot("Recon", 100))
        self.robots.append(Robot("Killshot", 100))

    # def add_robots(self):
    #     tank = Robot("Grunt", 200)
    #     scout = Robot("Recon", 100)
    #     sniper = Robot("Killshot", 100)
    
    #     self.robots.append(tank)
    #     self.robots.append(scout)
    #     self.robots.append(sniper)