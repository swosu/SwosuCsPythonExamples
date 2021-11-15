
import matplotlib.pyplot as plt
import random
x_values =[]
y_values = []

for index in range(1,26):
    coin = random.randint(0, 1)
    print('coin is: ', coin)
    print('index is: ', index)
    x_values.append(index)
    y_values.append(coin)

print('x values, ', x_values)
print('y values, ', y_values)
plt.scatter(x_values, y_values, color='darkgreen', marker='^')
plt.show()
