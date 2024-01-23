

def read_file(file_name):
    print('Opening the file: ', file_name)
    with open(file_name, 'r') as file:
        words = file.readlines()
    return words

def write_file(file_name, data):
    print('Opening the file: ', file_name)
    with open(file_name, 'w') as file:
        file.write(data+"\n")
    


if __name__ == "__main__":

    parks_jpgs = read_file("park_photos.txt")
    print(parks_jpgs)

    for park in parks_jpgs:
        park = park.replace('jpg', 'txt')

    parks_txts = ([park.replace('photo.jpg', 'info.txt') for park in parks_jpgs])
    print(parks_txts)

    file_rewrite = open("park_photos.txt", "w")
    for park in parks_txts:
        file_rewrite.write(park)

    file_rewrite.close()