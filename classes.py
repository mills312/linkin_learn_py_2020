
class Vehicle():
    def __init__(self, bodystyle="cart") -> None:
        self.n_bodystyle = bodystyle


class Car(Vehicle):
    def __init__(self, enginetype) -> None:
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype


class Truck(Vehicle):
    def __init__(self, enginetype) -> None:
        super().__init__("Truck")
        self.wheels = 4
        self.doors = 2
        self.enginetype = enginetype


class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar) -> None:
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.sheels = 2
        self.doors = 0
        self.enginetype = enginetype 


car1 = Car("gas")
car2 = Car("electric")
mtc1 = Motorcycle("gas", True)
print(" This vehicle is type: ", car1.n_bodystyle, ", with a ", car1.enginetype, " engine and has ", car1.doors, " door(s).")
print(" This vehicle is type: ", car2.n_bodystyle, ", with a ", car2.enginetype, " engine and has ", car2.doors, " door(s).")
print(" This vehicle is type: ", mtc1.n_bodystyle, ", with a ", mtc1.enginetype, " engine and has ", mtc1.doors, " door(s).")


