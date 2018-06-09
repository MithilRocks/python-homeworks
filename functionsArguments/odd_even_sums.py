def my_odd_even_sum(num):
    odd_sum, even_sum = 0, 0
    for i in num:
        i = int(i)
        if i & 1 == 1:
            odd_sum += i
        else:
            even_sum += i

    return odd_sum, even_sum

def ClassOddEvenDigitsSum(num):
    odd_sum, even_sum = 0, 0
    while num!=0:
        rem = num%10
        if rem & 1 == 1:
            odd_sum += rem
        else:
            even_sum += rem

        num = int(num/10)
    
    return odd_sum, even_sum

def main():
    num = eval(input("Enter your number: "))
    odd_sum, even_sum = ClassOddEvenDigitsSum(num)
    print("For number {} odd numbers sum is {} and even numbers sum is {}".format(num, odd_sum, even_sum))

if __name__ == "__main__":
    main()