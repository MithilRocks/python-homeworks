def push(l1, data):
    l1.append(data)

def pop(l1):
    return l1.pop()

def isEmpty(l1):
    return l1 == []

def isFull(l1):
    return len(l1) == 10

def peep(l1):
    return l1[-1]

def main():
    the_list = []
    while True:
        user_input = eval(input("Enter 1 to push number, 2 to pop, 3 to return last element and 4 to exit: "))

        if user_input == 1:
            number = eval(input("Enter your number to push: "))
            the_list.append(number)
            print("Updated list: {}".format(the_list))
        elif user_input == 2 and not isEmpty(the_list):
            print("Poped element is: {}".format(pop(the_list)))
        elif user_input == 3:
            print("Last pushed element is: {}".format(peep(the_list)))
        else:
            break

if __name__ == "__main__":
    main()