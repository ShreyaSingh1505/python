#reverse
str = str(input("Enter your string"))
rev=str[::-1]
print("the reverse of the string is :",rev)
if(rev==str):
    print("the string is palindrome")
else:
    print("the string is not palindrome")


