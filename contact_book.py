contact = {}

def display_contact():
    print("Name\t\tContact Number\tEmail_Address\tHome_Address")
    for key in contact:
        print(f"{key}\t\t{contact.get(key)}")

while True:
    choice = int(input("1. Add Contact \n2. Search Contact \n3. View Contact \n4. Update Contact \n5. Delete Contact \n6. Exit \n\n\n Your Choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        phone = int(input("Enter Phone Number: "))
        email_address = input("Enter Email Address: ")
        home_address = input("Enter Your Address: ")
        contact[name] = phone,email_address,home_address
    
         

    elif choice == 2:
        search_name = input("Enter the contact name: ")
        if search_name in contact:
            display_contact()
        else:
            print("The contact is not found.")

    elif choice == 3:
        if not contact:
            print("Empty Contact Book")
        else:
            display_contact()

    elif choice == 4:
        modify_contact = input("Enter the contact name to be edited: ")
        if modify_contact in contact:
            new_phone = input("Enter the number to be updated: ")
            new_email = input("Enter the Email ID to be updated: ")
            new_address = input("Enter the Address to be updated: ")
            contact[modify_contact] = (new_phone,new_email,new_address)
            print("Contact updated.")
            display_contact()
        else:
            print("The name is not present in the contact book.")

    elif choice == 5:
        del_contact = input("Enter the contact the you wish to delete: ")
        if del_contact in contact:
            confirm = input("Are you sure you wish to delete the contact? (Y/N)")
            if confirm == 'y' or confirm == 'Y':
                contact.pop(del_contact)
                print("The contact has been successfully deleted.")
            else:
                print("The contact is not found.")
    elif choice == 6:
            break
    else:
        print("Invalid Option, please select the correct option,")


