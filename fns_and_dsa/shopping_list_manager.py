def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter an item to add to list: ")
            shopping_list.append(item)
        elif choice == "2":
            item = input("Enter item to be removed from list: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print(f"{item} is not found in shopping list")
        elif choice == "3":
            if shopping_list:
                for item in shopping_list:
                    print(item)
            else:
                print("Your shopping list is empty")
        elif choice == "4":
            break
        else:
            print("Invalid input. Please select from 1 to 4")

        print()

if __name__ == "__main__":
    main()