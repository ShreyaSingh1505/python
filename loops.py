n=int(input("Enter the number"))
#Prime Number
count=0
for i in range(1,n+1,1):
    n=n%i
    count = count+1
if(count==2):
        print("prime number")
else:
        print("not a prime number")

#Factorial
fac=1
for i in range (1,n+1):
    fac=fac*i
print(fac)

#while Loop
i=1
while (i<=20):
    print(i)
    i=i+1

#fibonacci Series
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
    