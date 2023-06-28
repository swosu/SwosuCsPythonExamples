class Cashier_algorithm:
    def __init__(self):
        #print('well done, you have created a cashier algorithm object!')
        self.data = []
        self.item_purchased = ''
        self.purchase_total = 0.0
        self.user_payment = 0.0
        self.total_change = 0.0
        self.change_remaining = 0.0
        self.denominations = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
        self.denomination_totals = []

    def greet_user(self):
        print('Hello, and welcome to the cashier\'s algorithm.')

    def ask_user_what_they_purchased(self):
        #self.item_purchased = input('What are you purchasing today? \n')
        self.item_purchased = 'toilet seat'   
        print(f'it is a fine day to buying things. \nI hope you enjoy your {self.item_purchased}.')

    def ask_user_purchase_total(self):
        #self.purchase_total = round(float(input(f'how much did {self.item_purchased} cost today? \n')), 2)
        self.purchase_total = round(float(2.99), 2)
        print(f'You were able to purchase {self.item_purchased} for ${self.purchase_total}? Excellent!')

    def ask_user_how_much_cash_they_handed_over(self):
        while True:
            #self.user_payment = round(float(input(f'how much money did you hand over for {self.item_purchased} 
            # that cost {self.purchase_total}? \n')), 2)
            self.user_payment = round(float(50.01), 2)
            if self.user_payment >= self.purchase_total:
                print(f'You paid them ${self.user_payment} for {self.item_purchased} that cost ${self.purchase_total}? We can work with that.')
                break
            else:
                print('That is not enough to cover the bill.')

    def display_total_change(self):
        self.total_change = round( ( self.user_payment - self.purchase_total ) , 2)
        print(f'After you paid ${self.user_payment} for {self.item_purchased} that cost ${self.purchase_total}, \
            your change due is ${self.total_change}. ')
    
    def calculate_denomination_totals(self):




if __name__ == "__main__":

    teller = Cashier_algorithm()
    teller.greet_user()
    teller.ask_user_what_they_purchased()
    teller.ask_user_purchase_total()
    teller.ask_user_how_much_cash_they_handed_over()
    teller.display_total_change()    
    teller.calculate_denomination_totals()

    