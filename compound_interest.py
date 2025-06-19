p=float(input("Enter the principle amount"))
r=float(input("Enter the rate of interest"))
n=float(input("Enter the time period"))

c=(1+(r/100))**(n)
A=p*c
print("Compound interest is",A-p)