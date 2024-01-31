print("Welcome to tip calculator.")
total = float(input("What is the total bill? ₹"))
tip= int(input("What percentage of tip you eould like to give? 10, 12, or 15? "))
people = int(input("Total no of people? "))
a = (total)*(tip/100)
total = total+a
final = total/people
final = round(final,2)
print(f"Each person should pay:₹{final}")