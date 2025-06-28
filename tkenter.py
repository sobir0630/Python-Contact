import tkinter as tk
from tkinter import messagebox
from contact import load_contacts, add_contact, json_fayili

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = load_contacts(json_fayili)

        # Listbox kontaktlar uchun
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)
        self.refresh_contacts()

        # Qo'shish uchun entrylar
        self.first_name = tk.Entry(root)
        self.first_name.pack()
        self.first_name.insert(0, "First name")

        self.last_name = tk.Entry(root)
        self.last_name.pack()
        self.last_name.insert(0, "Last name")

        self.phone = tk.Entry(root)
        self.phone.pack()
        self.phone.insert(0, "Phone")

        self.group = tk.Entry(root)
        self.group.pack()
        self.group.insert(0, "Group")

        self.add_btn = tk.Button(root, text="Add Contact", command=self.add_contact_gui)
        self.add_btn.pack(pady=5)

    def refresh_contacts(self):
        self.listbox.delete(0, tk.END)
        for c in self.contacts:
            self.listbox.insert(tk.END, f"{c['first_name']} {c['last_name']} | {c['phone']} | {c['group']}")

    def add_contact_gui(self):
        contact = {
            "first_name": self.first_name.get(),
            "last_name": self.last_name.get(),
            "phone": self.phone.get(),
            "group": self.group.get(),
        }
        self.contacts.append(contact)
        # Faylga yozish
        import json
        with open(json_fayili, "w", encoding="utf-8") as f:
            json.dump(self.contacts, f, ensure_ascii=False, indent=4)
        self.refresh_contacts()
        messagebox.showinfo("Success", "Contact added!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()