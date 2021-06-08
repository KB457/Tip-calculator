print("Welcome to the tip calculator")

cost = float(input("What was the total bill? $"))
percentage = input("What percentage tip would you like to give? 10, 12 or 15?")
people = int(input("How many people to split the bill?"))


new_percentage = int(percentage) /100
TIPADD = cost * new_percentage 

total = cost + TIPADD

bill_per_person = total / people

final_total = round(bill_per_person, 2)
final_total = "{:.2f}".format(bill_per_person)
print(f"Each person shold pay: ${final_total}")
