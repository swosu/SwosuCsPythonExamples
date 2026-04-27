def sort_to_lowest():
    myint = ["number 1", "number 2", "number 3"]
    numList = [int(input(f"{name}: ")) for name in myint]
    numList.sort()
    print(numList[0])

#sort_to_lowest()


def sort_to_lowest2():
    prompt_messages = ["number 1", "number 2", "number 3"]
    try:
        num_list = [int(input(f"Enter {prompt}: ")) for prompt in prompt_messages]
    except ValueError:
        print("Please enter valid integers only.")
        return
    
    num_list.sort()
    print(f"The lowest number is: {num_list[0]}")

#sort_to_lowest2()


def sort_to_lowest3():
    myint = ["number 1", "nummber 2", "number 3"]
    numList = [int(input(f"{name}: ")) for name in myint]
    smallest = min(numList)
    print(smallest)

#sort_to_lowest3()