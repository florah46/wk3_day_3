def missing_number(lista, listb):

    x = list(set(lista) - set(listb))
    return print(x)
missing_number([1,2,3,4,5,6,7], [1,3,4,5])

