amt=float(input("Enter the actual price of the item"))
dis=int(input("Enter the discount percent"))
discount=(dis/100)*amt
final_amt= amt - discount
print("the final price of the item after discount is ->",final_amt)