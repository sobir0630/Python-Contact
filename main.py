from sys import exit
from termcolor import colored
from printer import print_menu, print_status
from contact import(
     add_contact, 
     show_all_contact, 
     search_contact, 
     delete_contact,
     update_contact, 
     load_contacts 
)



def main():
    contacts: list[dict] = load_contacts("contacts.json")
    
    while True:
        print_menu()

        choice = input(colored("Menu tanlang: ", 'yellow'))

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            show_all_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            update_contact(contacts)
        elif choice == '6':
            exit(0)
        else:
            if choice.isalpha():
                print_status("alphaerror")
            

if __name__ == "__main__":
    main()
