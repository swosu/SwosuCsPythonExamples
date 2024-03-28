'''
The idea is to simulate the natural selection of a group of mice.
When 20 mice are released into a habitat with a carrying capacity of 300, how does the population change?
The environment will either be sandy or grassy.
In a sandy environment, brown mice are less likely to be seen by predators.
In a grassy environment, gray mice are less likely to be seen by predators (due to shadows).
However, for the purposes of this problem, the trait for storing food is found only in gray mice.
Brown color will be a dominant gene.
Food storing will be a recessive gene.
'''
import random

generation_count = 0

class Environment:
    def __init__(self):
        self.terrain = ''
        self.set_terrain()
        self.mice = []
        self.populate_env()
        self.carrying_capacity = 500

    def set_terrain(self):
        terrain_options = ['A', 'B']
        chosen_terrain = input(f"What kind of environment would you like to populate?\nA) sandy\nB) grassy\n:")
        chosen_terrain = chosen_terrain.upper()
        if chosen_terrain in terrain_options:
            if chosen_terrain == 'A':
                self.terrain = 'sandy'
            elif chosen_terrain == 'B':
                self.terrain = 'grassy'
        else:
            self.set_terrain()

    def get_terrain(self):
        return self.terrain
    
    def add_mouse(self, mouse):
        self.mice.append(mouse)

    def kill_mouse(self, mouse):
        self.mice.remove(mouse)

    def get_mice(self):
        return self.mice

    def populate_env(self):
        num_of_mice = int(input("How many mice would you like to populate the area with?\n"))
        num_of_brown_mice = int(num_of_mice/2)
        num_of_gray_mice = int(num_of_mice/2)

        for mouse in range(num_of_brown_mice):
            new_mouse = Mouse("CC", "FF")
            self.add_mouse(new_mouse)

        for mouse in range(num_of_gray_mice):
            new_mouse = Mouse("cc", "ff")
            self.add_mouse(new_mouse)

    def add_children(self):
        adult_mice = []
        for mouse in self.get_mice():
            if mouse.adult:
                adult_mice.append(mouse)
        #for mouse in adult_mice:
            #print(mouse.color_genes)
        for mouse in range(0, len(adult_mice), 2):
            num_children = random.randint(6, 8)
            for _ in range(num_children):
                random_adult = random.choice(adult_mice)
                child = random_adult.generate_child(self)
                self.mice.append(child)

    def kill_old_mice(self):
        for mouse in self.get_mice():
            if mouse.generation >= 60:
                mouse.survive = False

    def simulate_generation(self):
        global generation_count
        user_choice = True
        child_mice = []
        adult_mice = []
        while user_choice:
            self.add_children()
            print(f"After reproducing, there are {len(self.get_mice())} mice in the environment")
            brown_mice = []
            gray_mice = []
            for mouse in self.get_mice():
                if 'C' in mouse.color_genes:
                    brown_mice.append(mouse)
                elif 'C' not in mouse.color_genes:
                    gray_mice.append(mouse)
            print(f"After reproducing, there are {len(brown_mice)} brown mice")
            print(f"After reproducing, there are {len(gray_mice)} gray mice")

            #elimination based on color and age
            for mouse in self.get_mice():
                if mouse.adult:
                    mouse.set_survive(self)
                if not 'C' in mouse.color_genes:
                    mouse.set_survive(self)
                elif not mouse.adult:
                    mouse.child_set_survive(self)
        
            #elimination based on food
            starving_mice = []
            if len(self.get_mice()) > self.carrying_capacity:
                print("in starving if statement")             
                while len(starving_mice) < ((len(self.get_mice())) - self.carrying_capacity):
                    print("in starving while loop")
                    for mouse in self.get_mice():
                        if 'F' not in mouse.food_cache_genes:
                            mouse.fifty_fifty_chance()
                        elif 'F' in mouse.food_cache_genes:
                            mouse.twenty_five_percent_chance()

                        if not mouse.get_survive():
                            starving_mice.append(mouse)
        
            dead_mice = []
            for mouse in starving_mice:
                if mouse in self.get_mice():
                    mouse.survive = False            
            
            for mouse in self.get_mice():           
                if not mouse.survive:
                    dead_mice.append(mouse)

            for mouse in dead_mice:
                if mouse in self.get_mice():
                    self.kill_mouse(mouse)            
            
            '''for mouse in self.get_mice():
                if isinstance(mouse, Child):
                    mouse.__class__ = Mouse'''

            for mouse in self.get_mice():
                mouse.mature()
                


            generation_count += 1
            print(f"After {generation_count} generation...")
            print(f"There are now {len(self.get_mice())} mice in the environment.")
            brown_mice = []
            gray_mice = []
            for mouse in self.get_mice():
                if 'C' in mouse.color_genes:
                    brown_mice.append(mouse)
                elif 'C' not in mouse.color_genes:
                    gray_mice.append(mouse)
            print(f"After dying, there are {len(brown_mice)} brown mice")
            print(f"After dying, there are {len(gray_mice)} gray mice")

            user_choice = input("Would you like to run another generation?\n:")
            if user_choice in ['y','Y','yes','Yes']:
                user_choice = True
            else:
                user_choice = False


class Mouse:
    def __init__(self, color_genes, food_cache_genes):
        self.color_genes = color_genes
        self.food_cache_genes = food_cache_genes
        self.survive = True  
        self.generation = 0
        self.adult = False
    
    def get_survive(self):
        return self.survive
    
    def fifty_fifty_chance(self):
        survival_chance = random.randint(1,2)
        if survival_chance == 1:
            self.survive = True
        elif survival_chance == 2:
            self.survive = False

    def twenty_five_percent_chance(self):
        survival_chance = random.randint(1, 4)
        if survival_chance == 1:
            self.survive = True
        elif survival_chance in range(2,4):
            self.survive = False

    def one_third_chance(self):
        survival_chance = random.randint(1, 3)
        if survival_chance == 1:
            self.survive = True
        elif survival_chance in range(2,3):
            self.survive = False

    def set_survive(self, environment):
        #elimination based on color
        if 'C' in self.color_genes and environment.get_terrain() == 'sandy':
            self.fifty_fifty_chance()
        elif self.color_genes == 'cc' and environment.get_terrain() == 'sandy':
            self.one_third_chance()
        elif 'C' in self.color_genes and environment.get_terrain() == 'grassy':
            self.one_third_chance()
        elif self.color_genes == 'cc' and environment.get_terrain() == 'grassy':
            self.fifty_fifty_chance()   

    def two_fifth_chance(self):
        survival_chance = random.randint(1, 5)
        if survival_chance in range(1,2):
            self.survive = True
        elif survival_chance in range(3, 5):
            self.survive = False

    def child_set_survive(self, environment):
        #elimination based on color
        if 'C' in self.color_genes and environment.get_terrain() == 'sandy':
            self.twenty_five_percent_chance()
        elif 'c' in self.color_genes and environment.get_terrain() == 'sandy':
            self.two_fifth_chance()
        elif 'C' in self.color_genes and environment.get_terrain() == 'grassy':
            self.two_fifth_chance()           
        elif 'c' in self.color_genes and environment.get_terrain() == 'grassy':
            self.twenty_five_percent_chance()   

    def random_gene_select(self):
        color_gene_select = random.randint(1,2)
        if color_gene_select == 1:
            color_gene = self.color_genes[0]
        elif color_gene_select == 2:
            color_gene = self.color_genes[1]

        food_gene_select = random.randint(1,2)
        if food_gene_select == 1:
            food_gene = self.food_cache_genes[0]
        elif food_gene_select == 2:
            food_gene = self.food_cache_genes[1]

        return color_gene, food_gene  

    def generate_child(self, environment):
        eligible_mice = [mouse for mouse in environment.get_mice() if mouse.adult]
        if len(eligible_mice) < 2:
            return None  # not enough eligible mice to produce a child
        parent1, parent2 = random.sample(eligible_mice, 2)
        color_gene1, food_gene1 = parent1.random_gene_select()
        color_gene2, food_gene2 = parent2.random_gene_select()
        #child_color_genes = random.choice([color_gene1, color_gene2])
        #child_food_genes = random.choice([food_gene1, food_gene2])
        child_color_genes = [color_gene1, color_gene2]
        child_food_genes = [food_gene1, food_gene2]
        return Mouse(child_color_genes, child_food_genes)
    
    def mature(self):
        self.generation += 1
        if self.generation >= 1:
            self.adult = True

    


def main():
    experiment_env = Environment()
    experiment_env.simulate_generation()
    
    
    


if __name__ == "__main__":

    main()