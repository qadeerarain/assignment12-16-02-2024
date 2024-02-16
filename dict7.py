7.# Restaurant Menu Parser:
# import csv

def read_menu(file_path):
    menu = {}

    try:
        with open(file_path, 'r') as file:
            if file_path.endswith('.csv'):
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 3:
                        item, price, category = row
                        menu[item] = {'price': float(price), 'category': category}
            else:
                for line in file:
                    item, price, category = line.strip().split(',')
                    menu[item] = {'price': float(price), 'category': category}

        return menu

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

def browse_by_category(menu):
    categories = set(item['category'] for item in menu.values())
    print("\nCategories:")
    for category in categories:
        print(category)

    selected_category = input("Enter the category to browse: ")
    
    items_in_category = [item for item, details in menu.items() if details['category'] == selected_category]
    
    if items_in_category:
        print(f"\nItems in {selected_category} category:")
        for item in items_in_category:
            print(f"{item}: ${menu[item]['price']:.2f}")
    else:
        print(f"No items found in {selected_category} category.")

def search_item(menu):
    search_query = input("Enter the item name to search: ")

    matching_items = [item for item in menu.keys() if search_query.lower() in item.lower()]

    if matching_items:
        print("\nMatching items:")
        for item in matching_items:
            print(f"{item}: ${menu[item]['price']:.2f} ({menu[item]['category']})")
    else:
        print(f"No items found matching '{search_query}'.")

def main():
    file_path = input("Enter the path to the menu file (text or CSV): ")
    menu = read_menu(file_path)

    if menu:
        while True:
            print("\nOptions:")
            print("1. Browse by Category")
            print("2. Search for Item")
            print("3. Quit")

            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                browse_by_category(menu)

            elif choice == '2':
                search_item(menu)

            elif choice == '3':
                print("\nExiting the program. Goodbye!")
                break

            else:
                print("\nInvalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()