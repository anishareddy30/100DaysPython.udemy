print("welcome ")
bill = float(input(f"what was the total bill ? "))
tip = int(input("how much tip would you like to give ? 10 , 15 , 20 "))
people = int(input("how many people to spilt the bill"))

tip_amount = bill * tip / 100
total_bill = bill + tip_amount
each_person = total_bill / people

print(f"Each person should pay {each_person}")