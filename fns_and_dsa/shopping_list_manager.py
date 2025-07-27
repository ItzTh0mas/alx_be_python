shopping_list = []

def display_menu():
    print("\nMenu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item to add: ").strip()
        shopping_list.append(item)
        print(f"{item} added.")

    elif choice == "2":
        item = input("Enter item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed.")
        else:
            print("Item not found.")

    elif choice == "3":
        if not shopping_list:
            print("Shopping list is empty.")
        else:
            print("\n Shopping List:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")

    elif choice == "4":
        print("Exiting.")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
 
