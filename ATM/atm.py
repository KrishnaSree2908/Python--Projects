balance = 1000

# PIN check
pin = 1234
user_pin = int(input("Enter your PIN: "))

if user_pin != pin:
    print("Incorrect PIN. Access Denied.")
    exit()

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Invalid amount")
        else:
            balance += amount
            print("Amount deposited successfully")

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount")

        elif amount > balance:
            print("Insufficient balance")

        else:
            balance -= amount
            print("Please collect your cash")

    elif choice == 4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")
