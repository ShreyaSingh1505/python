w1=2
w2=3
w3=5
marks_1=float(input("Enter the marks 1 "))
marks_2=float(input("Enter the marks 2 "))
marks_3=float(input("Enter the marks 3 "))
total=w1+w2+w3
weighted_average=(w1*marks_1 + w2*marks_2 + w3*marks_3)/total
print("weighted average is -->",weighted_average)