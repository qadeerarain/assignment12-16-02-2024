
#2. Grade Calculator:
#overall grade based on a grading scale stored in a dictionary

def display_shopping_list(shopping_list):
    print("\nShopping List:")
    for item, checked in shopping_list.items():
        status = " [X]" if checked else " [ ]"
        print(f"{item}{status}")

def add_item(shopping_list, item):
    shopping_list[item] = False
    print(f"\n{item} added to the shopping list.")

def remove_item(shopping_list, item):
    if item in shopping_list:
        del shopping_list[item]
        print(f"\n{item} removed from the shopping list.")
    else:
        print(f"\n{item} not found in the shopping list.")

def check_off_item(shopping_list, item):
    if item in shopping_list:
        shopping_list[item] = True
        print(f"\n{item} checked off in the shopping list.")
    else:
        print(f"\n{item} not found in the shopping list.")

def main():
    shopping_list = {}

    while True:
        print("\nOptions:")
        print("1. Display Shopping List")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Check Off Item")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_shopping_list(shopping_list)
        elif choice == '2':
            item = input("Enter the item to add: ")
            add_item(shopping_list, item)
        elif choice == '3':
            item = input("Enter the item to remove: ")
            remove_item(shopping_list, item)
        elif choice == '4':
            item = input("Enter the item to check off: ")
            check_off_item(shopping_list, item)
        elif choice == '5':
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
