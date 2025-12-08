#Ch9_Rd2_HW_3of3_ShonH, 26.1 Lab: Simple Car
#Given two integers that represent the miles to drive forward and the miles to drive in reverse as user inputs, create 
# a SimpleCar object that performs the following operations:

#Drives input number of miles forward
#Honks the horn
#Reports car status
#Drives input number of miles in reverse
#Honks the horn
#Reports car status

class SimpleCar:
    def __init__(self):
        self.miles = 0

    def drive(self, dist):
        self.miles = self.miles + dist
       
    def reverse(self, dist):
        self.miles = self.miles - dist
       
    def get_odometer(self):
        return self.miles
   
    def honk_horn(self):
        print('beep beep')

    def vroom_driving_noise(self):
        print('vroom vroom')
       
    def report(self):
        print(f'Car has driven: {self.miles} miles')
       
if __name__ == "__main__":
    # TODO: Create SimpleCar object
    tacoma = SimpleCar()
    # TODO: Drive input number of miles forward
    tacoma.drive(float(input("Enter miles to drive forward: ")))
    # TODO: Honk the horn
    tacoma.honk_horn()
    tacoma.vroom_driving_noise()
    # TODO: Report car status
    tacoma.report()
    # TODO: Drive input number of miles in reverse
    tacoma.reverse(float(input("Enter miles to drive in reverse: ")))
    # TODO: Honk the horn
    tacoma.honk_horn()
    tacoma.vroom_driving_noise()
    # TODO: Report car status
    tacoma.report()