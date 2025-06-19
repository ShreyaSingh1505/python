#1.check whether given number is positive, negative or zero.
num=float(input("Enter the number "))
if num>0:
    print("The number is positive")
elif num<0:
    print("The number is negative")
else:
    print("The number is zero")

#2.Print larget of three number
a=float(input("Enter the number "))
b=float(input("Enter the number "))
c=float(input("Enter the number "))
if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
else:
    print("C is greater")

#3.check if a year is leap or not
year=int(input("Enter the number "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("The year is a leap year")
        else:
            print("The year is not a leap year")
    else:
        print("The year is a leap year")
else:
    print("The year is not a leap year")

#4. Uppercase and lowercase
string=str(input("Enter the string"))
if (string.isupper()):
    print(string.lower())
elif (string.islower()):
    print(string.upper())
else:
    print(string)

#5.calculator
num1=float(input("Enter the value"))
num2=float(input("Enter the value"))
print("enter operation: 1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
ch=str(input("Enter the operation you want to perform"))
if ch=="Additon":
    print(num1+num2)
elif ch=="Subtraction":
    print(num1-num2)
elif ch=="Multiplaction":
    print(num1*num2)
elif ch=="Division":
    print(num1/num2)
else:
    print("Enter valid operation")

#6.character is vowel or not
char=input("Enter the character")
if char in "aeiouAEIOU":
    print("Entered character is a vowel")
else:
    print("Entered character is not a vowel")

#7.Age category
age=int(input("Enter the age"))
if 0<age<12:
    print("Child")
elif 12<age<19:
    print("Teenager")
elif 19<age<58:
    print("Adult")
elif 58<age:
    print("Senior Citizen")
else:
    print("Enter Valid Age")

#8.week days
num=int(input("Enter number from 1 to 7"))
if num==1:
    print("Monday")
elif num==2:
    print("Tuesday")
elif num==3:
    print("Wednesday")
elif num==4:
    print("Thursday")
elif num==5:
    print("Friday")
elif num==6:
    print("Saturday")
elif num==7:
    print("Sunday")
else:
    print("Invalid number")