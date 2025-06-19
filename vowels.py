def count_vowels(text):
    
    vowels="aeiouAEIOU"
    count= 0
    for char in text:
        if char in vowels:
            count=count+1
    return count
    
string=str(input("Enter your string"))
print(count_vowels(string))
    


