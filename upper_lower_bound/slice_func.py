def my_slice(my_string, start, end, step = 1):
    sliced = ''

    if step >= 1:
        if start >= end:
            return ''
        elif end >= len(my_string):
            end = len(my_string) 
    elif step < 1:
        if end >= start:
            return ''
        elif start >= len(my_string):
            start = len(my_string) - 1

    for j in range(start, end, step):
        sliced += my_string[j]

    return sliced

if __name__ == "__main__":
    my_string = input("Enter string to slice: ")
    print("Sliced String is: ",my_slice(my_string, 30, 20, -2))