def anagram(s1,s2):
    return sorted(s1) == sorted(s2)
str1="listen"
str2="silent"
print(anagram(str1,str2))  