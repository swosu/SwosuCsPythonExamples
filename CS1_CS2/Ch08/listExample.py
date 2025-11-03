print('hello')

nums2 = [5, 6, 7, 8, 3]

for list_address in range(1, 6):
    print('our list_address is', list_address)
    print('small number', nums2[list_address - 1])
    print('large number', nums2[list_address])

    if nums2[list_address - 1] > nums2[list_address]:
        print('Not in order')
