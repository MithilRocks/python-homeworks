# HW: write a method similar to dict.fromkeys() but the values are individually assigned to every key

def my_from_keys(my_list, my_elements):
    my_dict = {}
    x, y = 0, 0

    while x < len(my_list):

        if y >= len(my_elements):
            my_dict[my_list[x]] = None
        else:
            my_dict[my_list[x]] = my_elements[y]
            y += 1
        
        x += 1
    
    return my_dict

def main():
    a = eval(input("Enter your list of keys: "))
    b = eval(input("Enter your list of values: "))
    print("Your dictionary is: {} ".format(my_from_keys(a,b)))

if __name__ == "__main__":
    main()
        