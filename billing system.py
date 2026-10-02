print("------ SHOP BILLING SYSTEM ------")

total = 0

while True:
    print("\nEnter item details")

    item = input("Item name: ")

    try:
        price = float(input("Price: "))
        if price <= 0:
            print("❌ Price must be greater than 0")
            continue
    except:
        print("❌ Invalid price input")
        continue

    try:
        quantity = int(input("Quantity: "))
        if quantity <= 0:
            print("❌ Quantity must be greater than 0")
            continue
    except:
        print("❌ Invalid quantity input")
        continue

    cost = price * quantity
    total += cost

    print(f"✅ {item} added | Cost = {cost}")

    more = input("Add another item? (yes/no): ").lower()
    if more != "yes":
        break

print("\n------ FINAL BILL ------")
print(f"Total Amount = {total}")
print("Thank you for shopping! 🛍️")