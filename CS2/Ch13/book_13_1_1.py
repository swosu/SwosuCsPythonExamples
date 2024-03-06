class Item:
    def __init__(self):
        self.name = ''
        self.quantity = 0

    def set_name(self, nm):
        self.name = nm

    def set_quantity(self, qnty):
        self.quantity = qnty

    def display(self):
        print(self.name, self.quantity)


class Produce(Item):  # Derived from Item
    def __init__(self):
        Item.__init__(self)  # Call base class constructor
        self.expiration = ''

    def set_expiration(self, expir):
        self.expiration = expir

    def get_expiration(self):
        return self.expiration
    
    def display(self):
        Item.display(self)  # Call base class display method
        print(f'  (Expires:({item2.get_expiration()}))')

class Bread(Produce):
    def __init__(self):
        Produce.__init__(self)
        self.carbs = 0

    def set_carbs(self, carb):
        self.carbs = carb

    def get_carbs(self):
        return self.carbs
    
    def display(self):
        Produce.display(self)
        print(f'  (Carbs:({our_bread.get_carbs()}))')

item1 = Item()
item1.set_name('Smith Cereal')
item1.set_quantity(9)
item1.display()

item2 = Produce()
item2.set_name('Apples')
item2.set_quantity(40)
item2.set_expiration('May 5, 2012')
item2.display()

our_bread = Bread()
our_bread.set_name('Whole Wheat')
our_bread.set_quantity(12)
our_bread.set_expiration('May 5, 2012')
our_bread.set_carbs(20)
our_bread.display()