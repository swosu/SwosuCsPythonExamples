import random

class Island_Population:
    def __init__(self):
        self.population = []
        self.female_mature = 0
        self.female_immature = 0
        self.male_mature = 0
        self.male_immature = 0
        

    def print_rabbit_age_information(self):
        for rabbit in self.population:
            rabbit.print_data()
            if rabbit.reproductive_maturity:
                if rabbit.female:
                    self.female_mature += 1
                else:
                    self.male_mature += 1
            else:
                if rabbit.female:
                    self.female_immature += 1
                else:
                    self.male_immature += 1
        print(
            "Mat Fem: ", self.female_mature, 
            "Immat Fem: ", self.female_immature, 
            "Mat M: ", self.male_mature,
            "Imma M: ", self.male_immature,
            "\nComp Total Pop: ", self.male_mature + self.male_immature + self.female_mature + self.female_immature,
            "\nTot Pop: ", len(self.population))

        

class Rabbit:
    def __init__(self, life_expectancy = 96, female = False):
        self.months_old = 0
        self.life_expectancy_in_months = 0
        self.female = female
        self.reproductive_maturity = False

    def print_data(self):
        print("individual rabbit data:")
        print(
            "Age: ", self.months_old, 
            "Life Expectancy: ", self.life_expectancy_in_months,
            "female?: ", self.female,
            "Reproductive Maturity: ", self.reproductive_maturity)

    def update_reproductive_maturity(self):
        #if the rabbit is female and is at least 5 months old, then it is reproductively mature
        # otherwise, it is not reproductively mature. 
        # if the rabbit is male, and it is at least 8 months old, then it is reproductively mature
        # otherwise, it is not reproductively mature.
        if self.female and self.months_old >= 5:
            self.reproductive_maturity = True
        elif not self.female and self.months_old >= 8:
            self.reproductive_maturity = True
        else:
            self.reproductive_maturity = False


if __name__ == "__main__":

    # set my random seed as 42
    random
    random.seed(42)
    # create an array of rabbit objects
    island_1 = Island_Population()


    # create a single female rabbit that has an age of 0 months and  has a random life expectancy between 0 and 144 months
    island_1.population.append(Rabbit(random.randint(0,144), True))
    print("after adding a single female:")
    # print off our current rabbit data:
    for rabbit in island_1.population:
        rabbit.print_data()

    # print off our current rabbit population size:
    print("after adding our female, our current population size is: ", len(island_1.population))

    # create a single male rabbit that has an age of 0 months and  has a random life expectancy between 0 and 144 months
    island_1.population.append(Rabbit(random.randint(0,144), False))

    # print off our current rabbit population size:
    print("after adding our male, our current population size is: ", len(island_1.population))

    # now we are going to manually increase the age of our rabbits by 1 month
    for rabbit in island_1.population:
        rabbit.months_old += 1
        rabbit.update_reproductive_maturity()

    # print off our current rabbit population size:
    print("after one month, our current population size is: ", len(island_1.population))

    # print off how old our bunnies are
    island_1.print_rabbit_age_information()
