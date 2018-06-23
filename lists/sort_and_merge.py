# HW: Wap to accept two lists from user, sort them using bubble sort and then merge them in sorted manner

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

def my_merge(a, b):
    a = my_sort_bubble(a)
    b = my_sort_bubble(b)
    new_list = []
    i,j = 0,0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            new_list.append(a[i])
            i += 1
        elif a[i] > b[j]:
            new_list.append(b[j])
            j += 1
        elif a[i] == b[j]:
            new_list.append(a[i])
            new_list.append(a[j])
            i, j = i+1, j+1

    if i < len(a):
        new_list.extend(a[i:])
    
    if j < len(b):
        new_list.extend(b[j:])
    
    return new_list

def main():
    a = eval(input("Enter the first list: "))
    b = eval(input("Enter the second list: "))
    print(my_merge(a,b))

if __name__ == "__main__":
    main()