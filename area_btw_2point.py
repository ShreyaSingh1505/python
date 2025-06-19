import math
x1=float(input("Enter the x coordinate first of the first point "))
x2=float(input("Enter the x coordinate second  of the first point"))
y1=float(input("Enter the y coordinate first of the first point "))
y2=float(input("Enter the xy coordinate second  of the first point "))
distance=math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("The distance between the two points is ",distance)