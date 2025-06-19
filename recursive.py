"""#sum of n natural numvbers using recursion
def rec_sum(n):
    if(n<0):
        return "enter positve number"
    elif(n==0):
        return 0
    else:
        return n + rec_sum(n-1)
n=5
print(rec_sum(n))

#factorial using recursion
def fac(n):
    if(n<0):
        return "enter positive number"
    elif(n==0):
        return 1
    else:
        return n * fac(n-1)
n=int(input("Enter positive number"))
print(fac(n))

#fibonacci series using recursion 
def fib(n):
    if (n<0):
        print("enter positive number")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
n=int(input("Enter the range:"))
for i in range(n):
    print(fib(i),end=" ")

#gcd using recursion 
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
print(gcd(24,12))

#sum of digits of a number using recurison
def sum_digit(n):
    if(n==0):
        return 0
    else:
        return (n%10) + sum_digit(n//10)
print(sum_digit(1234))   

#lamda function(even or odd)
num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
even=filter(lambda x:x%2==0,num)
odd=filter(lambda x:x%2!=0,num)
print(list(even))
print(list(odd))

#square of number using lambda
n=float(input("Enter the value"))
square=(lambda n:n**2)
print(square(n))  

#larger of two number using lambda
n=int(input("Enter value"))
m=int(input("Enter value"))
larger=lambda n,m:m if m>n else n
print(larger(n,m))  

#product of two numbers using lamda
n=float(input("Enter the value"))
m=float(input("Enter the value"))
product=(lambda n,m:n*m)
print(product(n,m))"""

#tem_celcius_fahrenhit
"""def celsius_to_fahrenheit(celsius_list):
    fahrenheit_list = [(temp * 9/5) + 32 for temp in celsius_list]
    return fahrenheit_list

celsius_temps = [0, 20, 100, -40, 37]
fahrenheit_temps = celsius_to_fahrenheit(celsius_temps)
print(fahrenheit_temps)"""

#capatalize the first letter of each word in a list of string

def capitalize_words(strings_list):
    capitalized_list = [string.title() for string in strings_list]
    return capitalized_list

strings = ["hello world", "python programming", "capitalize each word"]
capitalized_strings = capitalize_words(strings)
print(capitalized_strings)

#write a program to find a square of all no. in a list using math function
import math
def square_numbers(math_func, numbers_list):
    squared_list = [math_func(num, 2) for num in numbers_list]
    return squared_list

numbers = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(math.pow, numbers)
print(squared_numbers)

#use math function with lambda function to add corresponding elements of two list
def add_lists(list1, list2):
    return list(map(lambda x, y: x + y, list1, list2))

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
result = add_lists(list1, list2)
print(result)

#filter out sring of length less than 5 from a list using filter function 
def filter_short_strings(strings_list):
    return list(filter(lambda s: len(s) <= 5, strings_list))

strings = ["apple", "hi", "banana", "sun", "grape", "wow"]
filtered_strings = filter_short_strings(strings)
print(filtered_strings)

#use filter function to find all prime nmber in a list
"""def prime(n):
    count=0
    for i in range(1,n+1,1):
        
        if n%i==0:
            count=count+1
        elif count<0:
            print("number is not prime")
        else:
            continue
    
    if count==2:
        print("prime")
    else:
        print("not prime")
def filter_prime_numbers(numbers_list):
    return list(filter(prime, numbers_list))

# Example usage:
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 23]
prime_numbers = filter_prime_numbers(numbers)
print(prime_numbers)"""
       



 

































