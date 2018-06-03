def odd_even_sum(num):
    odd_sum, even_sum = 0, 0
    for i in num:
        i = int(i)
        if i & 1 == 1:
            odd_sum += i
        else:
            even_sum += i

    print("For number {} odd numbers sum is {} and even numbers sum is {}".format(num, odd_sum, even_sum))

if __name__ == "__main__":
    num = input("Enter your number: ")
    odd_even_sum(num)
    