#Name: Sumit Sohal
#Student id : c0902846
#Date: 27th Oct, 2023
#Program: creating a contact list by using add, view, update, search and delete personal contacts.

contacts = []

# Add a contact
def add_contact():
    contact_name = input("Enter Contact name: ")
    contact_phone = input("Enter Contact number: ")
    contact_email = input("Enter Email address: ")
    contact_add = input("Enter Address: ")
    
    # Created a list to store it in the dictionary
    contact = {
        'name': contact_name,
        'phone': contact_phone,
        'email': contact_email,
        'address': contact_add,
    }
    
    contacts.append(contact)
    print("Contact added successfully!\n")

#view all contacts

def view_contact():
    if len(contacts) == 0:
        print("\n No contact details are found.\n")
    else:
        for i in range (len(contacts)):
            print(f"name: {contacts[i]['name']}")
            print(f"phone no.: {contacts[i]['phone']}")
            print(f"email: {contacts[i]['email']}")
            print(f"address: {contacts[i]['address']}")
            print()


#update a contact

def update_contact():
    if not contacts:
        print("contact details not found.\n")
        return
    
    search_name = input("enter name of the contact you want to update: ")
    matching_contacts = []
    
    for contact in contacts:
        if search_name == contact['name']:
            matching_contacts.append(contact)

    if not matching_contacts:
        print("contact details not found.\n")
        return
    elif len(matching_contacts) == 1:
        contact = matching_contacts[0]

        print("update Menu:")
        print("1. Update Name")
        print("2. Update Phone Number")
        print("3. Update Email")
        print("4. Update Address")
        print("5. Cancel")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            new_name = input("Enter new name: ")
            contact['name'] = new_name
            print("Name updated. !\n")
        elif choice == '2':
            new_phone = input("Enter new phone no.: ")
            contact['phone'] = new_phone
            print("Phone number updated.\n")
        elif choice == '3':
            new_email = input("Enter new email: ")
            contact['email'] = new_email
            print("Email updated.\n")
        elif choice == '4':
            new_address = input("Enter new address: ")
            contact['address'] = new_address
            print("Address updated. \n")
        elif choice == '5':
            return
        else:
            print("Invalid. Please try again.\n")
    else:
        print("Many contacts found with the same name.\n")

# Function to delete a contact
def delete_contact():
    if not contacts:
        print("\n contacts not found.\n")
        return

    search_name = input("Enter the name of the contact you want to delete: ")
    matching_contacts = []

    for contact in contacts:
        if search_name == contact['name']:
            matching_contacts.append(contact)

    if not matching_contacts:
        print("Contact not found.\n")
        return
    elif len(matching_contacts) == 1:
        contact = matching_contacts[0]
        contacts.remove(contact)
        print("Contact deleted successfully!\n")
    else:
        print("Many contacts found with the same name. Please specify your search.\n")


# Function to search for a contact
def search_contact():
    if not contacts:
        print("\nNo contacts found.\n")
        return

    search_term = input("Enter the name here that you want to search for: ")
    found_contacts = []

    for contact in contacts:
        if search_term in contact['name']:
            found_contacts.append(contact)

    if not found_contacts:
        print("No matching contacts are found.")
    else:
        print("\nMatching contacts:")
        for i in range(len(found_contacts)):
            print(f"Name: {found_contacts[i]['name']}")
            print(f"Phone Number: {found_contacts[i]['phone']}")
            print(f"Email: {found_contacts[i]['email']}")
            print(f"Address: {found_contacts[i]['address']}")
            print()


def main():
    while True:
        print("/n *** Phone Book *** /n")
        print("1. Add a contact")
        print("2. View all contacts")
        print("3. Update a contact")
        print("4. Delete a contact")
        print("5. Search a contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            #Add a contact
            add_contact()

        elif choice == '2':
            #View all contacts
            view_contact()

        elif choice == '3':
            #Update all contacts
            update_contact()

        elif choice == '4':
            #Delete a contact
            delete_contact()

        elif choice == '5':
            #Search a contact
            search_contact()
            
        elif choice == '6':
            return

        else:
            print("Invalid choice. Please select a valid option (1,2,3,4,5,6).")

main()