#6. Phonebook Organizer:
# Create a program that stores names and phone numbers in a dictionary. Offer options to 
#add, search, and update contacts.
def add_contact(contacts, name, phone_number):
    contacts[name] = phone_number
    print(f"\nContact {name} with phone number {phone_number} added.")

def search_contact(contacts, name):
    if name in contacts:
        print(f"\nContact Found - {name}: {contacts[name]}")
    else:
        print(f"\nContact not found for {name}.")

def update_contact(contacts, name, new_phone_number):
    if name in contacts:
        contacts[name] = new_phone_number
        print(f"\nContact {name} updated with new phone number {new_phone_number}.")
    else:
        print(f"\nContact not found for {name}.")

def main():
    contacts = {}

    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter the contact name: ")
            phone_number = input("Enter the phone number: ")
            add_contact(contacts, name, phone_number)

        elif choice == '2':
            name = input("Enter the contact name to search: ")
            search_contact(contacts, name)

        elif choice == '3':
            name = input("Enter the contact name to update: ")
            new_phone_number = input("Enter the new phone number: ")
            update_contact(contacts, name, new_phone_number)

        elif choice == '4':
            print("\nExiting the program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
            if __name__ == "__main__":
    main()