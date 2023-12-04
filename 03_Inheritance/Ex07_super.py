from __future__ import annotations

class ContactList(list["Contact"]):
    def search(self, name: str) -> list["Contact"]:
        matching_contacts: list["Contact"] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts
    
class Contact:
    all_contacts = ContactList()
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.email!r}" f")"
        )
    
    def update_contact_details(self, name: str, email: str) -> None:
            self.name = name
            self.email = email
    
class Friend(Contact):
    def __init__(self, name: str, email: str, phone: str) -> None:
        super().__init__(name, email)
        self.phone = phone

    def __repr__(self) -> str:
        base_repr = super().__repr__()
        return f"{base_repr[:-1]}, {self.phone!r})"

    def update_details(self, new_name: str, new_email: str, new_phone: str) -> None:
        # Manipulate or validate the new_name
        if not new_name.startswith("Mr. ") and not new_name.startswith("Ms. "):
            new_name = "Mr./Ms. " + new_name  # Prefixing the name for example

        # Call the superclass method after manipulating the name
        super().update_contact_details(new_name, new_email)
        self.phone = new_phone

if __name__ == "__main__":
    f = Friend("Dusty", "Dusty@private.com", "555-1212")
    print(Contact.all_contacts)

    f.update_details('Rafael', 'myemail@private.com', "333-2222")
    print(Contact.all_contacts)


    