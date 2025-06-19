#create a list of number from 1-20 that are either divisible by 2 or 4
list=[]
for i in range(1,21):
    if i%2==0 or i%4==0:
        list.append(i)
print(list)

##create a list of number from 1-20 that are either divisible by 2 or 4 using filter function
list=list(filter(lambda x:x%2==0 or x%4==0,range(1,11)))
print(list)

#using filter function to a list of squares of numbers from 1-10,then using for statement in construct to sum the elements in the list generated.
list=list(filter(lambda x:x,map(lambda x:x**2,range(1,11))))
print(list)
sum=0
for i in list:
    sum+=i
print("sum of the elements of the list",sum)

#define a list of countries that are members of brics 
brics=["india","south africa","russia","china","brazil"]
print(brics)
country=input("enter country")
if country in brics :
    print("country is a member of brics")
else:
    print("country is not a member of brics")

#create a list of number in range 1-10 then delete all the even no. from the list and print the final list 
list2=filter(lambda x: x,range(1,11))
list1=[]
for i in list2:
    if i%2!=0:
        list1.append(i)
print(list1)

#print index at which a particular value adjust ,if value adjust at multiple location in the list then print all indices  also count the no. of times that values is repeated in the list.
list=[1,2,3,4,5,2,6,7,8]
val=int(input("print num"))
indices=[]
for i in range(len(list)):
    if list[i]==val:
        indices.append(i)
print("indices of the value",indices)

count_value=list.count(val)
print("value is repeated",count_value,"times")

#WAP that creates a list of words by combing the words in two individual list
list1=["hello","harry"]
list2=["world","potter"]
list3=[]
for i in list1:
    for j in list2:
        list3.append(i+j)
print(list3)

#WAP that form a list of first character of every words in every words in another list
list=["hello","world","python","java","c++"]
list1=[]
for i in list:
    list1.append(i[0])
print(list1)

#write a program to remve all duplicated from a list.
list=[1,2,2,3,3,3,4,5,]
xoxo=tuple(list)
print(xoxo)
yuvi=set(xoxo)
print(yuvi)

#write a program that a list of function that scale each element in the list by a factor of 10
def scale(list):
    return [i*10 for i in list]
list=[1,2,3,4,5]
print(scale(list))

#list has only positive number 
list1=[1,2,-4,-7,0,-9,5,7]
positive_number=list(filter(lambda x : x>=0,list1))
print(positive_number)

#changing uppercase into lowercase of strings in a list
list1=["HELLO","WOrld","NINja","hattORI"]
lowercase=list(map(lambda x : x.lower(),list1))
print(lowercase)

#list of square of numbers in the range 1 to 10
square=list(map(lambda x: x**2,range(1,11)))
print(square)

#list comprhension(combined list)

list1=[10,25,30]
list2=[20,30,50,60]
list3=[(x,y) for x in list1 for y in list2 if y%x==0]
print(list3)

              





