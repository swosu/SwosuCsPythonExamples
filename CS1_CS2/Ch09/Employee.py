class Employee:
    def __init__(self, name, wage=8.25, hours=20):
        """
        Default employee is part time (20 hours/week)
        and earns minimum wage
        """
        self.name = name
        self.wage = wage
        self.hours = hours

    def print_pay_info(self):
        print(f'{self.name} earns {self.wage:.2f} per hour and works {self.hours} hours per week')

    # ...


todd = Employee('Todd')  # Typical part-time employee
jason = Employee('Jason')  # Typical part-time employee
tricia = Employee('Tricia', wage=12.50, hours=40)  # Manager employee
bob = Employee('Bob', hours=50, wage = 1)  # Full-time employee

bob.print_pay_info()

employees = [todd, jason, tricia, bob]

for e in employees:
    print (f'{e.name} earns {e.wage*e.hours:.2f} per week')