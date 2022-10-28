class whats_left:
    def __init__(self):
        self.score_input = []
        self.counter = 0
        self.singles_array = []

    def load_input_score(self, incoming_score):
        self.score_input = incoming_score
        print(f'incoming scores is: {self.score_input}')


    def number_input_finder(self):
        for i in self.score_input:
            
            self.counter += 1

            if i == 0:
                self.singles_array.append(self.counter)
        print('singles with no scores:', self.singles_array)

##Unit Testing
    def counter_test(self):
        self.load_input_score([2,0,3,0,5,6])
        self.number_input_finder()
        print(self.singles_array)
        if [2, 4] == self.singles_array:
            print('test passed')
        else:
            print('test failed')
        

if __name__ == '__main__':
    our_object = whats_left()
    our_object.counter_test()

    
else:
    print('you imported upperpad_whats_left')








