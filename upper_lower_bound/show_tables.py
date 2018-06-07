def show_tables(lb, ub):
    for i in range(lb, ub+1):
        print("The table of {} is: ".format(i))
        for j in range(1, 11):
            print("{} * {} = {}".format(i,j,i*j))

if __name__ == "__main__":
    lb = eval(input("Enter lower bound: "))
    ub = eval(input("Enter upper bound: "))

    if lb > ub:
        print("Lower bound should be less than upper bound")
    else:
        show_tables(lb, ub)