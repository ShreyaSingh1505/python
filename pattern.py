#pattern 1
for i in range(1,7):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

#pattern 2
for i in range(1,6):
    for j in range(1,7-i):
        print("*",end=" ")
    print()

#pattern 3
for i in range (65,71):
    for j in range(65,i+1):
        print(chr(j),end=" ")
        j+1
    print()


#pattern 4
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#pattern 5
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#pattern 6
n=1
row=int(input("Enter the number"))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(n,end=" ")
        n+=1
    print()