class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "animal sound"
class Flyable:
    def fly(self):
        return "flying in the air"
class Bird(Animal,Flyable):
    def __init__(self,name,species):
        Animal.__init__(self, name)
        self.species = species
    def speak(self):
        return f"{self.name} says chirp "

bird = Bird("eagle","Birds of prey")
print(bird.speak())
print(bird.fly())
