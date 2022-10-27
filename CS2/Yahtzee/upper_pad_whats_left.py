
class whats_left:
    def __init__(self, dice_input):
        self.dice_input = dice_input
        self.counter = 0
        self.singles_array = []

    def no_input_finder(self):
        for i in self.dice_input:
            
            self.counter += 1

            if i == 0:
                self.singles_array.append(self.counter)
        print('singles with no scores:', self.singles_array)

example_input = [2,0,3,0,5,6]


if __name__ == '__main__':
    w1 = whats_left(example_input)
    w1.no_input_finder()
else:
    print('you have imported upper_pad_whats_left')   











