class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print(self.name,"is",self.age,"years old")


obj = Dog("Goofy",3)
obj.show()
print(obj.age)

obj1 = Dog("Tommy", 5)
obj1.show()
print(obj1.name)