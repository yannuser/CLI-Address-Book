from contact import Contact
import json

class AddressBook:
    """Manages a collection of Contact objects with CRUD operations and JSON persistence."""

    def __init__(self, storage = 'contacts.json'):
        self.contacts = []
        self.storage = storage

    def add_contact(self, contact):
        """Add a new Contact object to the list."""
        self.contacts.append(contact)
        print(f"Contact added")
        print("\n" + "-"*30 + "\n")

    def delete_contact(self, name):
        """Delete a  Contact object to the list."""
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact deleted")
                print("\n" + "-"*30 + "\n")
                return
        print("No matching contact found")
        print("\n" + "-"*30 + "\n")

    def find_contact(self, query):
        """Search Contact object in the list using name or email"""
        for contact in self.contacts:
            if contact.name.lower() == query.lower() or contact.email.lower() == query.lower():
                print("Contact found!")
                print(contact)
        print("\n" + "-"*30 + "\n")

    def list_contacts(self):
        """List all Contact object created."""
        if len(self.contacts) > 0:
            for i in range(len(self.contacts)):
                print(self.contacts[i])
        else:
            print("Nothing to show")
        print("\n" + "-"*30 + "\n")

    def save_to_file(self):
        """Save list of Contact Object in Json file"""
        with open(self.storage, 'w') as f:
            stock = []
            for contact in self.contacts:
                stock.append({"name": contact.name, "phone": contact.phone, "email": contact.email})
            json.dump(stock, f)

    def load_from_file(self):
        """Load datas from Json file to the list"""
        try:
            with open(self.storage, 'r') as f:
                data = json.load(f)
                # print("JSON data loaded successfully")
                # print(data)
                self.contacts = []
                for value  in data:
                    self.contacts.append(Contact(value["name"], value["phone"], value["email"]))
                print("Loaded successfully")
        except FileNotFoundError:
            print("No saved contacts yet. Starting fresh.")
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from '{self.storage}'. Check for syntax errors in the JSON.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        print("\n" + "-"*30 + "\n")
