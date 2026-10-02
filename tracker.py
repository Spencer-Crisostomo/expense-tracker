# Installment 2
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

item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print("\n" , "-" * 40)
print("SUMMARY")
print(f" - {item1}: \t ${amount1:.1f}")
print(f" - {item2}: \t ${amount2:.1f}")
print(f"Total spent: \t ${total:.1f}")
print(f"Average: \t ${average:.2f}")
print("-" * 40)

print("Made by: Clark Spencer O. Crisostomo | Installment 2")