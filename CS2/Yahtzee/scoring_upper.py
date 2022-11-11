
class whats_left:
    def __init__(self, dice_input):
        self.dice_input = dice_input
        self.counter = 0
        self.singles_array = []
        self.score_vector = []



    def no_input_finder(self):
        for i in self.dice_input:

            self.counter += 1

            if i == 0:
                self.singles_array.append(self.counter)
        print('singles with no scores:', self.singles_array)


if __name__ == '__main__':

    import dice_file
    import upperscore_scorepad
    upper_scorecard_object = upperscore_scorepad.singles_possible_scores()
    dice_object = dice_file.dice_class()
    dice_object.roll_new_five()
    upper_scorecard_object.load_input_dice(dice_object.dice_on_table)
    upper_scorecard_object.calculate_scores()
    upper_scorecard_object.print_upper_scorecard_options()




    w1 = whats_left(upper_scorecard_object.score_vector)

    w1.no_input_finder()
