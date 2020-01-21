class Character:
    def __init__(self, health, power):
        self.name = ""
        self.health = health
        self.power = power
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        if enemy.name == "zombie":
            pass
        else:
            enemy.health -= self.power
        print(f"{self.name} did {self.power}")
    def print_status(self):
        print(f"{self.name} has {self.health} and {self.power}") 
class Hero(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.name = "you"
   
    
    
       
          
class Goblin(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.name = "goblin"

class Zombie(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.name = "zombie"
    

  

def main():
    hero = Hero(10, 5)
    #goblin = Goblin(6, 2)
    goblin = Zombie(5, 5)
    while goblin.alive() and hero.alive():
        #print current hero and goblin status
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do? ")
        print(f"1. fight the {goblin.name}")
        print("2. do nothing")
        print("3. flee")

        user_input = input("> ")
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            if goblin.health <= 0:
                print("murdered the goblin")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Bye")
            break
        else:
            print(f"Invalid input{user_input}")

        if goblin.health > 0:
            #Goblin attacks
            goblin.attack(hero)
            if hero.health <= 0:
                print("You got murdered")

main()