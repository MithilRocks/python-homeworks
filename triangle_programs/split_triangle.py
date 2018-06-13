def split_triangle(level):
    spaces = level
    for x in range(1, level):
        side = "*" * x
        print(side+" " * (spaces * 2 - 3)+side)
        spaces -= 1
    print("*" * (level*2 - 1))
    

def main():
    split_triangle(10)

if __name__ == "__main__":
    main()