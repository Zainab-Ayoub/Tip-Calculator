print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
inDecimal = int(input("What percentage tip would you like to give? 10, 12, 0r 15?"))

inDecimal /= 100
percentage = bill * inDecimal 
addTipInBill = bill + percentage
addTipInBill /= people
addTipInBill = round(addTipInBill, 2)

print(f"Each person should pay: ${addTipInBill}")