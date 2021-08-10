class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        
    def weapon_specs(self):
        print("\nWeapon Name: ", self.name)
        print("Attack Power: ", self.attack_power)
