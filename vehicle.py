class vehicle:

    def __init__(self,name,features,price):
        self.name = name
        self.features = features
        self.price = price

    def show(self):
        print(self.name,self.features,"is",self.price,"$")
        
obj = vehicle("camero","650 hp-V8",76000)
obj.show()

obj1 = vehicle("lamborghini aventador","740 hp-V12",500000)
obj1.show()