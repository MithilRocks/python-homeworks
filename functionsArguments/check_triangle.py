def check_triangle(a, b, c):
    if (a+b) > c and (a+c) > b and (b+c) > a:
        return True
    else:
        return False

if __name__ == "__main__":
    a = eval(input("Enter first side length: "))
    b = eval(input("Enter second side length: "))
    c = eval(input("Enter third side length: "))

    if check_triangle(a, b, c):
        print("It is a triangle")
    else:
        print("It is not a triangle")