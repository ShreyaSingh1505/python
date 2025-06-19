str="Shreya Singh"
age=19
str1="is a good lady"

#converting string into uppercase
print(str.upper())

#convertng string into lowercase
print(str.lower())

#striping a string
print(str.strip())

#spliting a string(split into list of words)
print(str.split())

#using format method
print("My name is {} and I am going to be {} years old soon".format(str,age))

#using percent method  
print("My name is %s and I am going to be %d years old soon"%(str,age))

#using f string
print(f"My name is {str} and I am going to be {age} years old soon")

#concatenation
print(str+" "+str1)

#repaeatingstring 
print(str*3)

#join
print("  ".join(str))
print("*".join(str))

#replace
print(str1.replace("lady","girl"))

#startswith 
print(str.startswith("sh"))
print(str.startswith("Shreya"))
print(str.startswith("hreya"))
print(str.startswith("shreya"))

#endswith
print(str.endswith("ngh"))
print(str.endswith("singh"))
print(str.endswith("Singh"))
print(str.endswith("Shreya"))

#find(writes index of first letter in word)
print(str.find("Singh"))
print(str.find("Shreya"))
print(str.find("S"))
print(str.find("g"))

#count
print(str.count("a"))
print(str.count("S"))
print(str.count("h"))