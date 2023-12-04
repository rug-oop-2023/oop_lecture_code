class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def let_it_fly(obj):
    obj.fly()

# Duck Typing in action
bird = Bird()
airplane = Airplane()


if __name__ == "__main__":
    # Duck Typing example
    let_it_fly(bird)       # Outputs: Bird is flying
    let_it_fly(airplane)   # Outputs: Airplane is flying