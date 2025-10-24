# Tip Calculator Project
# Description
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay:
# (150.00/5) * 1.12 33.6
# After formatting the result to 2 decimal places = 33.60

# TotalBill is = 150
# tip = 12% .....12/100=0.12
print(150 * 0.12) #12% 0f 150
print(150 + 18) #final bill + tip
print(150 + 18 / 5)
print("each person should pay")
print(150/5* 1.12 ) #1st no of 150 and after that tip percent


# NOW WE ARE MAKING THE PROJECT TO CALCULATE THIS
print("welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("what percentage type of tip would you like to give? 10 12 15 "))
people = int(input("how many people to split the bill "))
bill_with_tip = (tip / 100 * bill + bill)
print(bill_with_tip)
#or
tip_as_percent = tip/100
total_tip_account = bill * tip_as_percent
total_bill = bill + total_tip_account 
print(total_bill)

bill_per_person = total_bill/ people
final_amount = round(bill_per_person , 2)
print(f"each person should pay$-{final_amount}")

