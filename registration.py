print("------ EVENT REGISTRATION SYSTEM ------")

participants = []

while True:
    print("\n1. Register")
    print("2. View Participants")
    print("3. Count Participants")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        
        if name.strip() == "":
            print("❌ Name cannot be empty")
        else:
            participants.append(name)
            print(f"✅ {name} registered successfully")

    elif choice == "2":
        if len(participants) == 0:
            print("No participants yet")
        else:
            print("\nParticipants List:")
            for p in participants:
                print("-", p)

    elif choice == "3":
        print("Total Participants:", len(participants))

    elif choice == "4":
        print("Exiting... Thank you!")
        break

    else:
        print("❌ Invalid choice")