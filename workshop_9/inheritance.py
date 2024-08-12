class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def display_info(self):
        print(f"{self.year} {self.make} {self.model} with {self.odometer_reading} kilometers on it.")

    def update_odometer(self, km):
        if km <= 0:
            print('Odometer must be positive')
            return
        self.odometer_reading += km


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size
        self.battery_current = battery_size * 0.9
    
    def charge_battery(self):
        if self.battery_size == self.battery_current:
            print('Battery is already full')
            return

        print('Battery is charging...')
        self.battery_current += 1

    def display_info(self):
        print(f"{self.year} {self.make} {self.model} with {self.odometer_reading} kilometers on it. It has a battery size of {self.battery_size} kWh.")


car = Car('Toyota', 'Corolla', 2019)
car.update_odometer(100_000)
car.display_info()

electric_car = ElectricCar('Tesla', 'Model S', 2020, 100)
electric_car.update_odometer(50_000)
for _ in range(11):
    electric_car.charge_battery()

electric_car.display_info()
print(electric_car.battery_current)
