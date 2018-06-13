def diamond_triangle(the_limit):
    y = (the_limit - 1) // 2 
    for x in range(1, the_limit + 1, 2):
        print(" " * y + "*" * x)
        y -= 1

    y = 1
    for z in range(x - 2, 0, -2):
        print(" "*y + "*" * z)
        y += 1

def main():
    diamond_triangle(10)

if __name__ == "__main__":
    main()