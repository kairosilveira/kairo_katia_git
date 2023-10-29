from car import Car

class ElectricCar(Car):
    def __init__(self, name, make, color, year, battery_p_mile = 1, battery_level = 100, mileage=0):
        self.battery_p_mile = battery_p_mile
        self.battery_level = battery_level
        super().__init__(name, make, color, year, mileage)

    def start(self):
        if self.battery_level==0:
            print("No battery, you can't start the car")
        else:
            return super().start()

    def drive(self, distance=10):
        self.battery_level -= distance*self.battery_p_mile
        return super().drive(distance)
