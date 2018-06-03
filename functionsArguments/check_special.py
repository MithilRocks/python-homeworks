def check_special(num):
    sum_of_cubes = 0
    for i in num:
        sum_of_cubes += int(i)**3
    
    if sum_of_cubes == int(num):
        return True
    else:
        return False

if __name__ == "__main__":
    num = input("Enter your number: ")
    if check_special(num):
        print("Your number {} is special!".format(num))
    else:
        print("Your number {} is not special!".format(num))
