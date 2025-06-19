#swap two numbers using temporary variable 

a=int(input("Enter the first no"))
b=int(input("Enter the second no"))
print("the numbers before swapping ", a,b)
t=a
a=b
b=t
print("the numbers after swapping ", a,b)