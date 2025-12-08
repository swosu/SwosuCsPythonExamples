#Ch9 HW Shon Hakanson, 9.12 Lab: Nutriotional Information (Classes/constructors)
class FoodItem():
    def __init__(self, name="water", fat=0.0, carbs=0.0, protein=0.0, num_servings=0.0):
        
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.num_servings = num_servings

       
    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories
       
    def print_info(self):
        print(f'Nutritional information per serving of {self.name}:')
        print(f'  Fat: {self.fat:.2f} g')
        print(f'  Carbohydrates: {self.carbs:.2f} g')
        print(f'  Protein: {self.protein:.2f} g')
    

if __name__ == "__main__":
    food_item = FoodItem()
    food_item.name = input("Input the name of the food item: ")
    if food_item.name == 'Water' or food_item.name == 'water':
        food_item.print_info()
        print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')                       
    
    else:
        food_item.fat = float(input("Input the amount of fat: "))
        food_item.carbs = float(input("Input the amount of carbohydrates: "))
        food_item.protein = float(input("Input the amount of protein: "))
        food_item.num_servings = float(input("Input the number of servings: "))
        
        food_item = FoodItem(food_item.name, food_item.fat, food_item.carbs, food_item.protein, food_item.num_servings)
        food_item.print_info()
        print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')
        print(f'Number of calories for {food_item.num_servings:.2f} serving(s): {food_item.get_calories(food_item.num_servings):.2f}')