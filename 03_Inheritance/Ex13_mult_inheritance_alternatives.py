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


# Options to use instead of multiple inheritance
# Standalone Python function for sending an email.

def send_mail(email: str, message: str) -> None:
    print(f"Sending mail to {email=}")
    # Add e-mail logic here




if __name__ == "__main__":
    e = Contact("John B", "johnb@sloop.net")
    print(Contact.all_contacts)
    send_mail(e.email, "Hello, test e-mail here")