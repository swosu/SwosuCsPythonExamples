# 13-7_HW_ShonH.py

class Pet:
    def __init__(self, name = "", age = 0):
        self.name = name
        self.age = age
   
    def print_info(self):
        print(f'Pet Information:')
        print(f'   Name: { self.name }')
        print(f'   Age: { self.age }')

class Cat(Pet):
    def __init__(self, name = "", age = 0, breed = ""):
        super().__init__(name, age)
        self.breed = breed

    def breed_info_added(self):
        super().print_info()
        print(f'   Breed: { self.breed }')

gen_pet = Pet(input("Input Pet Name: "), int(input("Input Pet Age: ")))
gen_pet.print_info()

cat_pet = Cat(input("Input Name of Cat: "), int(input("Input Cat Age: ")), input("Input Cat Breed: "))
cat_pet.breed_info_added()
