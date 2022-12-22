area_rect = lambda l,b:l*b
area_square =  lambda l:l*l
area_triangle = lambda h,w:0.5*h*w

l = int(input("Enter the length of square:"))
print(area_square(l))
l,b= input("Enter the length and width of rectangle:").split(" ")
print(area_rect(int(l),int(b)))
l,b= input("Enter the height and breadth of the triangle:").split(" ")
print(area_triangle(int(l),int(b)))
