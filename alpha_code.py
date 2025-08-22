class ElectricCar:
    def __init__(self, color='black', owner=None):
        self.color = color
        self.owner = owner

car1 = ElectricCar(color='yellow', owner='Gvido')

car2 = ElectricCar(owner='Gvido')

car3 = ElectricCar()

car4 = ElectricCar('yellow', 'Gvido')

car5 = ElectricCar('yellow')

car6 = ElectricCar(owner='Gvido', color='yellow')