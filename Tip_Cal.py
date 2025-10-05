print("Welcome to the tip calculator!") 
total_bill = float(input("What was the total bill? $\n"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
tip_amount = (tip/100)*total_bill
total = total_bill + tip_amount


Num=int(input("How many people to split the bill?\n")) 
split_amount = total_bill/Num
split_amount = round(split_amount, 2)
print(f"Each person should pay: {split_amount}")
