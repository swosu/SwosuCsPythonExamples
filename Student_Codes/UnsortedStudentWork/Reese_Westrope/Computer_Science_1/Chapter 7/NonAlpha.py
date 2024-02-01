words = input('Input whatever you want:\n')

list = []

for x in words:
    if x.isalpha() == True:
        list.append(x)

sentence = ''.join(list)

print(sentence)
