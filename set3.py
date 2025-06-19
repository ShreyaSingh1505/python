#area of cirlcle
dict={}
for key in range(5):
    key=int(input("Enter radius"))
    value=2*3.14*key
    dict[key]=value
print(dict)

#conversion
dict={}
dict1={}
for i in range(5):
    m=int(input("enter value"))
    value=m*100
    dict[m]=value
print(dict)
for j in range(5):
    cm=int(input("enter value"))
    value=cm/100
    dict1[cm]=value
print(dict1)

#dictionary for fibonacci number 
dict={}
n=int(input("enter number"))
f=n-1 + n-2

