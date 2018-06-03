def sum_of_digits(num):
    sum = 0
    for i in num:
        sum += int(i)
    return sum

if __name__ == "__main__":
    num = input("Enter your number: ")
    print("Sum of all numbers is: {}".format(sum_of_digits(num)))