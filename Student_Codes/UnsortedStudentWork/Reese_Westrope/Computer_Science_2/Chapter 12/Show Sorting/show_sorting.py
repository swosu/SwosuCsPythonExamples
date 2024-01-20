import json

def dict_conversion(list):
    dictionary = {
        list[item] : list[item +1] for item in range(0, len(list), 2)
    }
    return dictionary

def load_json_data(filename):
    with open(filename, 'r') as f:
        data = json.loads(f.read())
    return data

def save_to_json(filename, data):
    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent=1))

if __name__ == '__main__':

    show_dict = load_json_data("shows.json")

    print(show_dict)

    num_sorted_shows = sorted(show_dict.items(), key=lambda x: x[1], reverse=False)
    print(num_sorted_shows)
    #for show in sorted_shows:
	    #print(show[0], show[1])
            
    save_to_json("num_sorted_shows.json", num_sorted_shows)

    letter_sorted_shows = list(show_dict.keys())
    letter_sorted_shows.sort()
    print(letter_sorted_shows)

    save_to_json("letter_sorted_shows.json", letter_sorted_shows)

