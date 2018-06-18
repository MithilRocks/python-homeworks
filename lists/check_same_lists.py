# WAP to check if two lists are same
# list is heterogenous meaning it can contain multiple data types at once

def check_same_lists(a, b):

    if a != b:
        return False
        
    return True

def main():
    a = eval(input("Enter a list: "))
    b = eval(input("Enter a second list: "))

    if check_same_lists(a, b):
        print("The lists are same")
    else:
        print("The lists are not same")

if __name__ == "__main__":
    main()