names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny', 'Corbin']
index = int(input('which person would you like?'))

# Type your code here.
try:
    print('Name:', names[index] )
except IndexError  as excpt:
    print('Exception! {}'.format(excpt))
    if index < 0:
        print('The closest name is:', names[0])
    else:
        print('The closest name is:', names[len(names)-1])

"""
try:
    print('Name: {}'.format(names[index]))
except IndexError  as excpt:
    print('Exception! {}'.format(excpt))
    if index < 0:
        print('The closest name is: {}'.format(names[0]))
    else:
        print('The closest name is: {}'.format(names[9]))
"""
