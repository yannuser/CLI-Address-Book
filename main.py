"""main.py — Command-line interface for the Address Book app.

This script provides an interactive CLI to manage contacts using the AddressBook class.
Features include adding, searching, deleting, listing, and saving contacts to JSON.
"""


from contact import Contact
from address_book import AddressBook


def main():
    contactList = AddressBook()
    contactList.load_from_file()

    looping = True
    while looping:
        print("Address book started")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. View all")
        print("5. Exit\n")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        print("\n" + "-"*30 + "\n")

        match choice:
            case 1:
                name = input("Enter name: ")
                email = input("Enter email: ")
                phone = input("Enter phone number: ")

                c = Contact(name, phone, email)
                contactList.add_contact(c)
            case 2:
                query = input("Entrez le nom ou email du contact recherché")
                contactList.find_contact(query)
            case 3:
                name = input("Enter the name of contact to delete: ")
                contactList.delete_contact(name)
            case 4:
                contactList.list_contacts()
            case 5:
                contactList.save_to_file()
                looping = False
            case _:  
                print("Incorrect choice!")
                print("\n" + "-"*30 + "\n")


if __name__ == "__main__":
    main()