# find the roots of the quadritic equations
a=int(input("Enter the value"))
b=int(input("Enter the value"))
c=int(input("Enter the value"))
print("Quadritic Equation:",a,"x^2","+",b,"x","+",c)
d=b**2 - 4*a*c
den=2*a
if d>0:
    print("Quadritic Equation has real roots")
    root1=(-b+(d)**2)/den
    root2=(-b-(d)**2)/den
    print("Roots are",root1,root2)
elif d==0:
    print("Quadritic Equations have equal roots")
    root=(-b/den)
    print("Root of Quadritic equation is:",root)
else:
    print("Roots are imaginary.")

#character check

num=input("Enter the character")
#if num.isupper():
if ("A"<=num<="Z"):
    print("Character is uppercase")
#elif num.islower():
elif  ("a"<= num<="z"):
    print("Character is lowercase")
else:
    print("Character is numeric value")


