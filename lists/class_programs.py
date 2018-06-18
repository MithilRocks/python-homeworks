# wap to write an append function of our own

def my_append(a, b, position):
    return (a[:position] + b + a[position:])

# wap to print the indexes of all the occurences of the data in the list
def all_indexes(a, value):
    indexes = []
    x = 0
    while x < len(a):
        if a[x] == value:
            indexes.append(x)
        x += 1
    return indexes

# wap to accept a list from user and sort it without using built in sort
def my_sort_bubble(a):
    swap = True
    while swap:
        swap = False
        x = 0 
        while x < (len(a) - 1):
            if a[x] > a[x+1]:
                swap = True
                a[x], a[x+1] = a[x+1], a[x]
            x += 1
    return a

# HW: Wap to accept two lists from user, sort them using bubble sort and then merge them in sorted manner

# HW: WAP to accept two lists from user and return intersection, union, difference of them

# HW: WAP to accept a heterogenous nested list and make it single level list
 
def main():
    a = eval(input("Enter your list to sort: "))
    print("Sorted list is: {}".format(my_sort_bubble(a)))
    
if __name__ == "__main__":
    main()