
def count_down_recursive(count):
    if count == 0:            
        print('Go!')                  
    else:                        
        print(count)             
        count_down_recursive(count-1)      

def count_down_iterative(count):
    while count > 0:            
        print(count)
        count -= 1
    print('Go!')
     
if __name__ == '__main__':
    count_down_recursive(2)
    count_down_iterative(2)

