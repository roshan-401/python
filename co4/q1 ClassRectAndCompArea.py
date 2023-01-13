class Rectangle:

    def __init__(self,length,breadth):
        self.breadth = breadth
        self.length = length
    def area(self):
        return self.length * self.breadth

dimension1 = (input("Enter dimension of first rectangle: ").split(" "));
dimension2 = (input("Enter dimension of second rectangle: ").split(" "));

rectangle1 = Rectangle(int(dimension1[0]),int(dimension1[1]))
rectangle2 = Rectangle(int(dimension2[0]),int(dimension2[1]))


if(rectangle1.area() > rectangle2.area()):
    print("reactangle with length", rectangle1.length ,"and breadth",rectangle1.breadth," is bigger")
    print("ji")
else:
    print("reactangle with length", rectangle2.length ,"and breadth",rectangle2.breadth," is bigger")
    print("li");
    

