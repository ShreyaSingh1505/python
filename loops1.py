import math

#1.sum and average
n=int(input("Enter the number"))
sum=0
for i in range(1,n+1):
    sum =sum+i
print("sum of first n natural numbers is ",sum)
avrg=sum/n
print("The average of the first n natural number:",avrg)

#2. 20 horizontal star
for i in range(1,21):
    print("*",end=" ")

#3. sum from m to n
m=int(input("Enter number"))
n=int(input("Enter number"))
sum=0
for i in range(m,n):
    sum=sum+i
print("Sum of numbers from m to n is:",sum)

#4. Armstrong number
n=int(input("Enter the number"))
l=len(str(n))
sum=0
temp=n
while n>0:
    a=n%10
    sum=sum+(a)**l
    n=n//10

if sum == temp:
    print("The number is a armstrong number")
else:
    print("The number is not a armstrong number")

#5. Reverse number
n=int(input("enter number"))
rev=0
while n>0:
    a=n%10
    rev=rev*10+a
    n=n//10
print("reversed number is",rev)

#6. greatest common divisor
#print(math.gcd(48,24))
a=int(input("Enter number"))
b=int(input("Enter number"))
if(a>b):
    ted=a
else:
    ted=b
for i in range(1,ted+1):
    if(a%i==0 and b%i==0):
        gcd=i

print("GCD of",a,"and",b,"is:",gcd)

#7. countdown
n=int(input("Enter number"))
for i in range(n,-1,-1):
    print(i)

n=int(input("Enter number"))
for i in range(1,n+1,1):
    space=" "*((n+1)-i)
    star="*"*((2*i)-1)
    print(space+star)

n=int(input("enter number of rows:"))
#method-1
for i in range(1,n+1,1):
    space=" "*((n+1)-i)
    star="*"*((2*i)-1)
    print(star+space)
for i in range(n-1,0,-1):
    space=" "*((n+1)-i)
    star="*"*((2*i)-1)
    print(star+space)

#method-2
for i in range(1,n+1,1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,n+1,1):
    for j in range(1,(n+1)-i):
        print("*",end=" ")
    print()



        
