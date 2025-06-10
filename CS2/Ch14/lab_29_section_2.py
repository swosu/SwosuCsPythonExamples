# TODO: Write recursive reverse_string() function here.

def reverse_string(string):
    if len(string) == 1:
        print(f'our crrent string is {string} which has a length of {len(string)}.')
        return string
    else:
        print(f'now we are lookikng for the reverse of {string[1:]}')
        return reverse_string(string[1:]) + string[0]
if __name__ == "__main__":
    in_str = 'hello'
    result_str = reverse_string(in_str)
    print(f'Reverse of "{in_str}" is "{result_str}".')