def all_permutations(permList, nameList):
    size = len(nameList)
    #print('all permutations was called with name list size,', size)

    if size == 0:
        #print('if statement: size was 0')
        for i in range(len(permList)):
            print(permList[i], end=' ')
        print()
    else:
        for i in range(size):
            #print('else statement: size was:', i)
            newPerms = permList.copy()
            newPerms.append(nameList[i])
            newNames = nameList.copy()
            newNames.pop(i)
            print('new names is', newNames, end=' ')
            print('new Perms is', newPerms, '    ', end=' ')
            all_permutations(newPerms, newNames)

if __name__ == "__main__":
    print('paste in your list of names and press enter')
    nameList = input().split(' ')
    permList = []
    all_permutations(permList, nameList)
