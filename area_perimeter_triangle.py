#Program to find the perimeter and area of the triangle
import math
a=float(input("Enter the first side of the triangle"))
b=float(input("Enter the second side of the triangle"))
c=float(input("Enter the third side of the triangle"))
sum=a+b+c
print(f"perimeter of a traingle is{sum}")
s=sum/2
t=math.sqrt(s*(s-a)*(s-b)*(s-c))
#t= (s*(s-a)*(s-b)*(s-c))**0.5
print("area of the triangle is ", t) 
