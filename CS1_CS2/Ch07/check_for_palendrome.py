word_to_check = 'racecar'

reversed_word = word_to_check[ : : -1 ]

print(f'forwards it is {word_to_check} and backwards it is {reversed_word}.')

is_palendrome = True
# Iterate over index
for element in range(0, len(word_to_check)):
    #print(f'our index is: {element}.')
    #print(word_to_check[element])
    
    if word_to_check[element] != reversed_word[element]:
        #print('not a palendrome')
        is_palendrome = False
        
        
        
if not is_palendrome:
    print('this was not a pelendrome')
    
else:
    print('palendrome')
    
    

