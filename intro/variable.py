class car:
    wheels = 10

    def __init__(self):
        self.color = 'black'
        self.company = 'mahndra'
        self.mileage = 5
    
car1 = car()
car2 = car()

car2.color = 'red'

car.wheels = 5

print(car1.color,car1.company,car1.mileage,car1.wheels)
print(car2.color,car2.company,car2.mileage,car2.wheels)