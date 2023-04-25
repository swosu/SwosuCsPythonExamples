import json

gear_options = ['sleeping bag', 'ferro rod', 'fishing kit', 'pot', 'knife', 'axe', 'saw', 'food rations', 'gill net', 'paracord', '12X12 tarp', 'bow and 6 arrows', 'multitool', 'bivy bag', 'wire', 'water bottle', 'frying pan']

def print_list(list):
    for item in list:
        print(item)

class Participant:

    def __init__(self, name, gear):
        self.name = name
        self.gear = gear

    def save_to_json(self, filename):
        participant_dict = {'name': self.name, 'gear': self.gear}
        with open(filename, 'w') as f:
            f.write(json.dumps(participant_dict, indent=1))

    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())
        return data

def load_from_json(filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())
        return data

def save_to_json(filename, data):
    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent=1))

if __name__ == '__main__':

    chosen_gear = []
    participant_list = []
    


    print("You have been selected to participate in a competition of survival.")
    name = input("Enter your name.\n:")
    print(f"{name}, you will be allowed to choose five items from the following list to help you in this competition.")
    print_list(gear_options)

    for index in range(5):
        in_list = False
        item = input("Choose an item from the list above.\n:")
        while not in_list:           
            if item in gear_options:
                in_list = True
            else:
                item = input("We couldn't find that item in the list above.\nTry checking your spelling and capitalization and make your choice.\n:")
        chosen_gear.append(item)
        print("So far, you have chosen the following items:")
        print_list(chosen_gear)

    participant = Participant(name, chosen_gear)
    participant_list.append(participant)
    print(participant_list)
    #save_to_json("participants.json", participant_list)
    #print(participant.load_from_json("participants.json"))

    participant_list.append(load_from_json("participants.json"))
    print(participant_list)

    chosen_gear.clear()