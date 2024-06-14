# Tip Calculator

print("Welcome to the tip calculator!")
bill=float(input("what was your total bill? $"))
tip=int(input("what percentage tip would you like to give? 10, 12 or 15? "))
people=int(input("how many people to split the bill ?"))

bill_with_tip=tip/100 * bill + bill
print(f"Total bill with tip = ${bill_with_tip}")
each_person_pay=float(bill_with_tip/people)
print(f"Each person will pay = ${round(each_person_pay ,2)}")