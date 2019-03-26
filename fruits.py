class Fruits:
    def __init__(self,name):
        self.name = name
        if name == "green apple":
            self.healthy = True
        else:
            self.healthy = False
        self.different_taste = True
        self.from_plant = True
    
class Apple(Fruits):
    sweet = True
    spherical = True
    def ishealthy(self):
        return self.healthy
    def informaton(self):
        if self.sweet is True:
            print(self.name,"is sweet")
        else:
            print(self.name, "is not sweet")
        
        if self.spherical is True:
            print(self.name,"is spherical")
        else:
            print(self.name, "is not spherical")

apple_name = str(input("Enter the type of apple :"))
apple = Apple(apple_name)
if apple.ishealthy():
    print(apple.name, "is healthy")
else:
    print(apple.name,"is not healthy")

apple.informaton()
