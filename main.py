print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
inDecimal = int(input("What percentage tip would you like to give? 10, 12, 0r 15? "))
people = int(input("How many people to split the bill? "))


inDecimal /= 100
percentage = bill * inDecimal 
addTipInBill = bill + percentage
addTipInBill /= people
addTipInBill = round(addTipInBill, 2)
addTipInBill = "{:.2f}".format(addTipInBill)

print(f"Each person should pay: ${addTipInBill}")