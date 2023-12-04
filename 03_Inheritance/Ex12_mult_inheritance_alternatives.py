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
# Single inheritance and added the send_mail function to a subclass of Contact.
class EmailContact(Contact):
    def send_mail(self, message: str) -> None:
        print(f"Sending mail to {self.email=}")
        # Add e-mail logic here




if __name__ == "__main__":
    e = EmailContact("John B", "johnb@sloop.net")
    print(Contact.all_contacts)
    e.send_mail("Hello, test e-mail here")