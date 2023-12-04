class Contact:
    all_contacts: list["Contact"] = []

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.email!r}"
            f")"
        )


class Suplier(Contact):
    def order(self, order: "Order") -> None:
        print(f"Send this {order} order to {self.name}.")


class Order:
    pass


if __name__ == "__main__":
    c_1 = Contact("Dusty", "dusty@example.com")
    c_2 = Contact("Steve", "steve@itmaybeahackt.com")

    c = Contact("Some Body", "somebody@example.net")
    s = Suplier("Sup Plier", "supplier@example.net")

    print(c.name, c.email, s.name, s.email)

    from pprint import pprint
    pprint(c.all_contacts)

    # Supplier has the method order
    s.order("I need pliers")

    # Contact does not have the method order. E error message will appear.
    c.order("I need pliers")