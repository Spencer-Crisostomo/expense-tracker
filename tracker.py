# Installment 4
# Author: Clark Spencer O. Crisostomo
# Description: Expense tracker's landing page

print("=" * 40)
print("\t EXPENSE TRACKER")
print("\tTrack Your Expenses!")
print("=" * 40)

print("\nMAIN MENU")
print(" [1] Add an expense\t(coming soon)")
print(" [2] View all expenses\t(coming soon)")
print(" [3] Show total spent\t(coming soon)")
print(" [4] Exit\t\t(coming soon)\n")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

subtotal = 0

item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

print("\n" + "-" * 40)
print("SUMMARY")
print(f" - {item1}: \t${amount1:.1f}")
print(f" - {item2}: \t${amount2:.1f}")
print(f"Subtotal: \t${subtotal:.1f}")
print(f"Average: \t${average:.2f}")
print(f"Tax (12.0%): \t${tax:.1f}")
print(f"Grand total: \t${total:.1f}")

if over_budget:
    print(f"Over budget by ${-left:.1f}!")
elif total > budget * 0.90:
    print(f"Careful: only ${left:.1f} left")
else:
    print(f"Within budget. ${left:.1f} left")

print("-" * 40)
print("Made by: Clark Spencer O. Crisostomo | Installment 4")