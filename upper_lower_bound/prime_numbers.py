def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(n**0.5) + 1

    for j in range(3, sqr, 2):
        if n % j == 0:
            return False

    return True

def show_primes(lb, ub):
    for i in range(lb, ub):
        if is_prime(i):
            print(i)

def show_not_primes(lb, ub):
    for i in range(lb, ub):
        if not is_prime(i):
            print(i)

if __name__ == "__main__":
    lb = eval(input("Enter Lower Bound: "))
    ub = eval(input("Enter Upper Bound: "))

    if lb > ub:
        print("Lower Bound should be smaller than upper bound")
    else:
        print("All the prime numbers between {} and {}".format(lb,ub))
        show_primes(lb, ub)

        print("All the non-prime numbers between {} and {}".format(lb,ub))
        show_not_primes(lb, ub)