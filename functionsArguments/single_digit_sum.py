def sum_of_digits(num):
    sum = 0
    for i in num:
        sum += int(i)
        if sum > 10:
            sum = sum_of_digits(str(sum))
    return sum

if __name__ == "__main__":
    num = input("Enter your number: ")
    print("Single sum of all digits: {}".format(sum_of_digits(num)))
