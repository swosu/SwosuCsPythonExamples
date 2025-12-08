#Ch9 HW Shon Hakanson, Prob 9.16 Lab: Vending Machine

class VendingMachine:
    def __init__(self):
        self.bottles = 20
        
    def purchase(self, purchase_amount):
        self.bottles = self.bottles - purchase_amount
      
    def restock(self, restock_amount):
        self.bottles = self.bottles + restock_amount
    
    def get_inventory(self):
        return self.bottles
        
    def report(self):
        print(f'Inventory: {self.bottles} bottles')

if __name__ == "__main__":

    vend_mach = VendingMachine()
    
    vend_mach.purchase(int(input("Enter number of bottles to purchase: ")))

    vend_mach.restock(int(input("Enter number of bottles to restock: ")))

    vend_mach.report()