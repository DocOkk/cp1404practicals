"""Display even numbers, odd numbers or squares within inclusive bounds."""

MENU = "1. Show even numbers\n2. Show odd numbers\n3. Show squares\n4. Exit"
start_number = int(input("Start number: "))
end_number = int(input("End number: "))
print(MENU)
choice = input(">>> ")
while choice != "4":
    if choice == "1":
        for number in range(start_number, end_number + 1):
            if number % 2 == 0:
                print(number, end=" ")
        print()
    elif choice == "2":
        for number in range(start_number, end_number + 1):
            if number % 2 != 0:
                print(number, end=" ")
        print()
    elif choice == "3":
        for number in range(start_number, end_number + 1):
            print(number ** 2, end=" ")
        print()
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ")
print("Finished.")
