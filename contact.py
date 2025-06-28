from termcolor import colored
from printer import print_status, print_all_contact
import json

json_fayili = "contacts.json"

def load_contacts(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def add_contact(contacts: list[dict]):
    first_name = input(colored("first name: ", 'blue'))
    last_name = input(colored("last name: ", 'blue'))
    phone = input(colored("phone: ", 'blue'))
    group = input(colored("group (family, friend, work, other): ", 'blue'))

  
    contacts.append({
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "group": group,
    })
    with open(json_fayili, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)
    print_status('success')

def show_all_contact(contacts: list[dict]):

    if contacts:
        print_all_contact(contacts)
    else:
        print_status('allerror')

def search_contact(contacts: list[dict]):
    search = input(colored("frist name >> ", 'yellow')).strip().lower()
    contacts = [con for con in contacts if con["first_name"].lower() == search.lower()]
    if contacts:
        print_all_contact(contacts)
    else:
        print_status("fileerror")

def delete_contact(contacts):
    delete = input(colored("first name >> ", 'yellow')).strip().lower()
    found = False
    for contact in contacts[:]:
        if contact["first_name"].lower() == delete:
            contacts.remove(contact)
            found = True
    if found:
        print_status("delete")

    else:
        print_status("fileerror")



def update_contact(contacts):
    user = input(colored("choise contact >>"))
    found = False
    for contact in contacts:
        if contact["first_name"].lower() == user:
            contact["first_name"] = update_name = input(colored("new first name >> ")) or contact["first_name"]
            contact["last_name"] = update_last = input(colored("new last name >> ")) or contact["last_name"]
            contact["phone"] = update_phone = input(colored("new phone >> ")) or contact["phone"]
            contact["group"] =  update_group = input(colored("new group(family, friend, work, other) >> ")) or contact["group"]
            found = True
        with open(json_fayili, "w", encoding="utf-8") as f:
            json.dump(contacts, f, ensure_ascii=False, indent=4)
    if found:
        print_status("update")
    else:
        print_status("updateerror")



  
   



