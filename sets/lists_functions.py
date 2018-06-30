import copy

def list_add(my_list, element):
    if element not in my_list:
        my_list.append(element)

def list_difference(*args):
    final_list = args[0]

    if len(args) == 1:
        return final_list

    for other_list in args[1:]:
        for i in other_list:
            list_discard(final_list, i)

    return final_list

def list_intersection(a, b):
    final_list = []

    for x in a:
        if x in b:
            final_list.append(x)

    return final_list 

def list_union(*args):
    final_list = []

    for x in args:
        for i in x:
            if i not in final_list:
                final_list.append(i)
    
    return final_list

def list_discard(my_list, element):
    while True:
        if element in my_list:
            my_list.remove(element)
        else:
            break

def list_issubset(a,b):
    temp = []

    for x in a:
        if x in b:
            temp.append(x)

    if temp == a:
        return True
    
    return False

def list_issuperset(a,b):
    temp = []

    for x in b:
        if x in a:
            temp.append(x)

    if temp == b:
        return True
    
    return False

def list_isdisjoint(a,b):
    if list_intersection(a,b) == []:
        return True
    
    return False

def list_remove(a, element):
    if element in a:
        a.remove(element)
    else:
        raise KeyError('Element doesn\'t exist')

def list_symmetric_difference(a,b):
    final_list = copy.deepcopy(a)

    for x in b:
        if x in final_list:
            final_list.remove(x)
        elif x not in final_list:
            final_list.append(x)

    return final_list


a = [1,2,3,4,6]
b = [4,6,7,8,9]
print(list_symmetric_difference(a,b))