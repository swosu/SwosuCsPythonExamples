class Grill:
    menu = ['Hamburger', 'Cheeseburger', 'Hotdog', 'Fries', 'Soda']

    def __init__(self):
        self.data = []

    def order(self, order):
        self.data.append(order)

    def check_order(self):
        for item in self.data:
            if item in self.menu:
                print('You ordered a', item)
            else:
                print('We do not have', item)

if __name__ == '__main__':
    customer_one = Grill()

    customer_one.order('Hamburger')

    print(customer_one.data)

    customer_one.check_order()
