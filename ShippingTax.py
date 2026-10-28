'''
Created on Oct 27, 2026

@author: Day's PC
'''

# Shipping Tax Program
# Ask for the sale item price and destination state

price = float(input("Enter the sale item price: $"))
state = input("Enter the destination state: ").strip().upper()

if state == "TX" or state == "LA":
    shipping_tax = 1.25
elif state == "CA":
    shipping_tax = 3.25
else:
    shipping_tax = 0.50

print(f"Shipping tax: ${shipping_tax:.2f}")
