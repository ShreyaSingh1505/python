#For Reading a file
#file.txt is file taken for example
f=open('file.txt','r')
text=f.read()
print(text)
f.close()

#For writing in file

f=open('file.txt','w')
f.write("Hello World")
f.close()

# For appending in file

f=open('file.txt','a')
f.write("It is a python program")
f.close()

#Another method of opening a file 
with open("file.txt",'a') as f:
    f.write("recently participated in hackathon")




