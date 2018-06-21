# HW: WAP to accept a heterogenous nested list and make it single level list

def single_level(the_list):
    result = []
    for x in the_list:
        if type(x) is list:
            result.extend(single_level(x))
        else:
            result.append(x)

    return result

def main():
    a = eval(input("Enter your heterogenous list: "))
    print("Your single level list is: {}".format(single_level(a)))

if __name__ == "__main__":
    main()