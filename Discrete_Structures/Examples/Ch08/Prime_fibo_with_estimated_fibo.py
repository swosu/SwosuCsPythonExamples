import time




if __name__ == '__main__':
    # make a list of fibonacci numbers
    fibo = [0, 1]

    # spend 3 seconds making the list as long as possible
    start_time = time.time()
    time_difference = 0
    while time_difference < 0.001:
        current_time = time.time()

        time_difference = current_time - start_time
        
        
        fibo.append(fibo[-1] + fibo[-2])

        if len(fibo) % 10 == 0:
            print('time difference:', time_difference, 'seconds', end = ' ')
            print(' fibo length:', len(fibo), end = ' ')
            # print last 10 numbers
            print(fibo[-10:])


    # what was the largest number we calculated in fibo?
    max_fibo = fibo[-1]
    print('max_fibo:', max_fibo)

