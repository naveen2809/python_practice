class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def description(self):
        return f"{self.color} colored {self.model} car"

class MarutiCar(Car):    
    def __init__(self, model, color, dealer):
        super().__init__(model, color)
        self.dealer = dealer

    def description(self):
        return f"{self.color} colored Maruti Suzuki {self.model} car from dealer {self.dealer}"
    
    def get_dealer(self):
        return f"{self.dealer}"

car_1 = Car('Pizza', 'Red')
print(car_1.description())

car_2 = MarutiCar('Wagaon R', 'Brown', 'Varun Motors')
print("The dealer is "+car_2.get_dealer())

car_3 = MarutiCar('Vitara Brezza', 'Maroon', 'Nexa')
print(car_3.description())