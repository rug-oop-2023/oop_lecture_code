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


class MailSender:
    def __init__(self, email: str) -> None:
        self.email = email

    def send_mail(self, message: str) -> None:
        print(f"Sending mail to {self.email=}")
        # Add e-mail logic here

# Options to use instead of multiple inheritance
# Using composition instead of inheritance.
class EmailableContact(Contact):
    def __init__(self, name: str, email: str) -> None:
        super().__init__(name, email) 
        self.mail_sender = MailSender(email)    


if __name__ == "__main__":
    emailable_contact = EmailableContact("John B", "johnb@sloop.net")
    print(Contact.all_contacts)
    emailable_contact.mail_sender.send_mail("Hello, test e-mail here")