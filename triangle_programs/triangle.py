def triangle(the_limit):
    y = (the_limit - 1) // 2
    for x in range(1, the_limit + 1, 2):
        print(" " * y + "*" * x)
        y -= 1

def main():
    triangle(9)

if __name__ == "__main__":
    main()