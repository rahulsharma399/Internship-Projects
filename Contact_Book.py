class contact:
    def __init__(self, name, phone_number):  
        self.name = name
        self.phone_number = phone_number

class contactmanager:
    def __init__(self):
        self.contacts = []
    def load_contacts(self, contacts_list):
        for contact_data in contacts_list:
            new_contact = contact(contact_data["name"], contact_data["phone_number"])
            self.contacts.append(new_contact)

    def add_contact(self, name, phone_number): 
        new_contact = contact(name, phone_number)
        self.contacts.append(new_contact)  
        print(f"Contact {name} added successfully") 

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found")
        else:
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone number: {contact.phone_number}")

    def search_contact(self, name_or_phone_number):
        found = False
        for contact in self.contacts:
            if contact.name == name_or_phone_number or contact.phone_number == name_or_phone_number:
                print(f"Name: {contact.name}, Phone number: {contact.phone_number}") 
                found = True
                break
        if not found:
            print("Contact not found")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully")
                return
        print("Contact not found")

def main():
    provided_contacts = [
        {"name": "Akshar", "phone_number": "8218683575"}
    ]
    contact_manager = contactmanager()
    contact_manager.load_contacts(provided_contacts)
   
    while True:
        print("\n1. Add contact")
        print("2. View contacts")
        print("3. Search contacts")
        print("4. Delete contact")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            contact_manager.add_contact(name, phone_number)
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            name_or_phone_number = input("Enter name or phone number: ")
            contact_manager.search_contact(name_or_phone_number)
        elif choice == "4":
            name = input("Enter name: ")
            contact_manager.delete_contact(name)
        elif choice == "5":
            break
        else:
            print("exit")

if __name__== "__main__":
    main()
