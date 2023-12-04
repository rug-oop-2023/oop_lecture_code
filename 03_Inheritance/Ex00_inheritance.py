class Parent:
    def __init__(self, arg1):
        self.arg1 = arg1

class Children(Parent):
    def children_method(self):
        return f"{self.arg1} is used by the children class"

if __name__ == "__main__":    
    kid = Children("Abby")
    print(kid.children_method())