class Car:
    def __init__(self,name, make, color, year, mileage=0):
        self.name = name
        self.make = make
        self.color = color
        self.year = year
        self.mileage = mileage
        self.is_runnig = False


    def start(self):
        if not self.is_runnig:
            print("Starting car...")
            self.is_runnig = True
        else:
            print("The car is already on...")
        
    
    def drive(self, distance = 10):
        if self.is_runnig:
            print("Driving", distance,"miles...")
            self.mileage += distance
        else:
            print("You need to turn the car on first!")