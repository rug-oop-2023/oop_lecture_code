class Vehicle:
    def start_engine(self):
        print("Starting vehicle engine")

class Car(Vehicle):
    def start_engine(self):
        print("Starting car engine with advanced features")

if __name__ == "__main__":

    my_vehicle = Vehicle()
    my_vehicle.start_engine() 

    # Directly using the Car class, not through a Vehicle reference
    my_car = Car()
    my_car.start_engine()