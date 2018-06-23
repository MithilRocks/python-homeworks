# HW: WAP to accept two lists from user and return intersection, union, difference of them

def intersection(a, b):
    result = []
    for x in a:
        if x in b and x not in result:
            result.append(x)

    return result

def difference(a,b):
    result = []
    for x in a:
        if x not in b:
            result.append(x)
    
    return result

def union(a,b):
    result = a
    for x in b:
        if x not in result:
            result.append(x)

    return result

def main():
    a = eval(input("Enter first list: "))
    b = eval(input("Enter second list: "))

    inter = intersection(a,b)
    differ = difference(a,b)
    united = union(a,b)

    print("Intersection of the two lists is {}".format(inter))
    print("Difference of the two lists is {}".format(differ))
    print("Union of the two lists is {}".format(united))

if __name__ == "__main__":
    main()
