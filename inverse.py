def inverse(list_of_input):
    reversed_list = []

    for i in list_of_input[::-1]:
        if isinstance(i,list):
            reversed_list.append(inverse(i))
        else:
            reversed_list.append(i)
    return reversed_list




listem = [[1, 2], [3, 4], [5, 6, 7]]    

sonuc = inverse(listem)

print(sonuc)