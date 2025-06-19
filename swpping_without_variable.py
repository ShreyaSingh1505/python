#swap two number without using third variable 

a=int(input("Enter the first no"))
b=int(input("Enter the second no"))
print("the numbers before swapping ", a,b)
a=a+b
b=a-b
a=a-b
print("the numbers after swapping ", a,b)