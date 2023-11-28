


def flatten(list_of_input):
    result = []
    for item in list_of_input:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result




giris = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

sonuc = flatten(giris)

print(sonuc)



