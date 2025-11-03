
class TransportMode:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.location = "Earth"

    def info(self):
        print(f'Vehicle: {self.name} can go {self.speed} mph.')

class MotorVehicle(TransportMode):
    def __init__(self, name, speed, mpg):
        TransportMode.__init__(self, name, speed)
        self.mpg = mpg
        self.fuel_gal = 0 

    def add_fuel(self, amount):
        self.fuel_gal += amount

    def info(self):
        TransportMode.info(self)
        print(f'Fuel: {self.fuel_gal:f} gallons.  MPG: {
            self.mpg}.')

    def drive(self, distance):
        required_fuel = distance / self.mpg
        if self.fuel_gal < required_fuel:
            print('Not enough gas.')
        else:
            self.fuel_gal -= required_fuel
            print(f'{self.fuel_gal:f} gallons remaining.')

class Airplane(MotorVehicle):
    def __init__(self, name, speed, wingspan):
        self.wingspan = wingspan
        self.altitude = 0
        self.air_speed = 0
        TransportMode.__init__(self, name, speed)
        
    def fly(self):
        self.altitude = 30000
        self.air_speed = 500
        print('Flying is fun.')
    
    def info(self):
        TransportMode.info(self)
        print(f'Wingspan: {self.wingspan} feet.')

class MotorCycle(MotorVehicle):
    def __init__(self, name, speed, mpg):
        MotorVehicle.__init__(self, name, speed, mpg)

    def wheelie(self):
        print('That is too dangerous.')


scooter = MotorCycle('Vespa', 55, 40)
dirtbike = MotorCycle('KX450F', 80, 25)
airplane = Airplane('Cessna', 180, 40)

scooter.info()
dirtbike.info()
airplane.info()
choice = input('Select scooter (s),  dirtbike (d), or airplane (a): ')
if choice == 's':
    scooter.wheelie()
elif choice == 'd':
    dirtbike.drive(100)
elif choice == 'a':
    airplane.fly()
else:
    print('Invalid selection.')



