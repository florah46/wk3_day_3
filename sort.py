def x_sort(x):

    even =[]
    odd = []
    characters = []
    x_dict = dict()
    if not isinstance(x, list):
        return 'Error'

    if not x:
        x_dict["even"] = even
        x_dict["odd"] = odd
        x_dict ["chars"] = characters
        return dict
    
    for i in x:
        if isinstance(i, int):
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        elif isinstance(i, str):
            characters.append(i)
        
    x_dict['even'] = sorted(even)
    x_dict['odd'] = sorted(odd)
    x_dict['chars'] = sorted(characters)
    
    return x_dict
    
if __name__ == "__main__":
    print(x_sort([1, 4, 3,'m', 'f']))
    
