# Installment 5
# Author: Clark Spencer O. Crisostomo
# Description: Expense tracker's landing page

print("=" * 40)
print("\t EXPENSE TRACKER")
print("\tTrack Your Expenses!")
print("=" * 40)

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

count = 0 
choice = ""

print("\nMAIN MENU")
print(" [1] Add an expense")
print(" [2] View all expenses\t(coming soon)")
print(" [3] Show total spent")
print(" [4] Exit")

subtotal = 0

while choice != "4":

    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1

        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

    elif choice == "2":
        print("Coming soon: The tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        over_budget = total > budget
        left = budget - total

        print(f"  Expenses: \t{count}")
        print(f"  Subtotal: \t${subtotal:.1f}")
        print(f"  Tax: ({tax_percent:.1f}%):\t${tax:.1f}")
        print(f"  Grand total: \t${total:.1f}")

        if over_budget:
            print(f"Over budget by ${-left:.1f}!")
        elif total > budget * 0.90:
            print(f"  Careful: \tonly ${left:.1f} left")
        else:
            print(f"Within budget. ${left:.1f} left")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("=" * 40)
        print("Made by: Clark Spencer O. Crisostomo | Installment 5")
        print("=" * 40)

    else:
        print("  Please choose 1, 2, 3, or 4.")