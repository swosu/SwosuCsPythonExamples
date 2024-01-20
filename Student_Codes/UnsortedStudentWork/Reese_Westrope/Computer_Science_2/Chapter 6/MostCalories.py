class FoodItem:
    # TODO: Define constructor with arguments to initialize instance 
    #       attributes (name, fat, carbs, protein)
    def __init__(self, name, fat, carbs, protein, calories):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.calories = calories
       
    def get_calories(self, num_servings):
        # Calorie formula
        global calories
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories
       
    def print_info(self):
        print(f'Nutritional information per serving of {self.name}:')
        print(f'  Fat: {self.fat:.2f} g')
        print(f'  Carbohydrates: {self.carbs:.2f} g')
        print(f'  Protein: {self.protein:.2f} g')
        print(f'  Calories: {self.calories:.2f} g')

if __name__ == "__main__":

    CalorieList = []
    FoodList = []

    while  len(FoodList) < 3:
        item_name = input("What is your food?\n")
        if item_name == 'Water' or item_name == 'water':
            food_item = FoodItem(item_name, 0, 0, 0, 0)
            food_item.print_info()
            FoodList.append("water")
            CalorieList.append(food_item.get_calories(1.0))
            print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')                       
    
        else:
            amount_fat = float(input(f"How many grams of fat are in your food?"))
            amount_carbs = float(input("How many grams of carbs are in your food?"))
            amount_protein = float(input("How many grams of protein are in your food?"))
            amount_calories = (food_item.get_calories(1.0))
            num_servings = float(input("How many servings are you eating?"))
        
            food_item = FoodItem(item_name, amount_fat, amount_carbs, amount_protein, amount_calories)
            food_item.print_info()
            FoodList.append(item_name)
            CalorieList.append(food_item.get_calories(1.0))
            print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')
            print(f'Number of calories for {num_servings:.2f} serving(s): {food_item.get_calories(num_servings):.2f}')

    Food1 = FoodList[0]
    Food2 = FoodList[1]
    Food3 = FoodList[2]

    Calorie1 = CalorieList[0]
    Calorie2 = CalorieList[1]
    Calorie3 = CalorieList[2]

    if Calorie1 > Calorie2 and Calorie1 > Calorie3:
        print(f'Your highest calorie food is {Food1} and has {Calorie1} calories per serving')
    elif Calorie2 > Calorie1 and Calorie2 > Calorie3:
        print(f'Your highest calorie food is {Food2} and has {Calorie2} calories per serving')
    elif Calorie3 > Calorie1 and Calorie3 > Calorie2:
        print(f'Your highest calorie food is {Food3} and has {Calorie3} calories per serving.')

