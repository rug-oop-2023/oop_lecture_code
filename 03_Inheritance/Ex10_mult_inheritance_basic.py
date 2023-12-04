class Father:
    def __init__(self):
        self.father_name = "Father"

    def hobby(self):
        return "Fishing"

class Mother:
    def __init__(self):
        self.mother_name = "Mother"

    def hobby(self):
        return "Gardening"

class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        self.child_name = "Child"

if __name__ == "__main__":
    # Creating an instance of Child
    child = Child()

    print(child.child_name)   # Outputs: Child
    print(child.father_name)  # Outputs: Father
    print(child.mother_name)  # Outputs: Mother

    # In case of method resolution order, it will take the first occurrence, which is from Father
    print(child.hobby())      # Outputs: Fishing