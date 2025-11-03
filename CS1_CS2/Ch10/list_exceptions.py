if __name__ == "__main__":
    names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
    
    try:
        index = int(input())
        print(f"Name: {names[index]}")
    except IndexError as e:
        print(f"Exception! {e}")
        if index < 0:
            print(f"The closest name is: {names[0]}")
        else:
            print(f"The closest name is: {names[-1]}")
