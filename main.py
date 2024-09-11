currentAge = int(input("What is your currect age? "))

daysInCurrentAge = currentAge * 365
weeksInCurrentAge = currentAge * 52
monthsInCurrentAge = currentAge * 12

daysInNinetyYears = 90 * 365
weeksInNinetyYears = 90 * 52
monthsInNinetyYears = 90 * 12

daysLeft = daysInNinetyYears - daysInCurrentAge
weeksLeft = weeksInNinetyYears - weeksInCurrentAge
monthsLeft = monthsInNinetyYears - monthsInCurrentAge

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} left.")