class Scorepad_class:
    def __init__(self):
        self.data = []


if __name__ == '__main__':
    print('running scorepad to load a score')

    print('what are the dice on the table?')
    import dice_file
    dice_object = dice_file.dice_class()
    dice_object.roll_new_five()

    print('what is the score options?')
    import upperscore_scorepad
    upper_scorecard_object = upperscore_scorepad.singles_possible_scores()
    upper_scorecard_object.load_input_dice(dice_object.dice_on_table)
    upper_scorecard_object.calculate_scores()
    upper_scorecard_object.print_upper_scorecard_options()

    scorecard_object = Scorepad_class()