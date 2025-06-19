#using global keyword 
a=13
def shreya():
    global a
    a=11
    print("local variable is ",a)
    y=9
    print("second local variable",y)
shreya()
print("the global variable is",a)
