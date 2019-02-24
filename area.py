#ask length and breadth
length = int(input("Enter the length of rectangle: "))
breadth = int(input("Enter the breadth of rectangle : "))
area = length*breadth
print("Area of the rectangle is ", area)

#we are checking with if condition...
if area < 100:
    print("area is less than 100") # we are printing less than 100
elif area == 100:
    print("area is equal to 100")
else:
    print("area is more than 100")
