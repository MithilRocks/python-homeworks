def up_side_down_triangle(the_limit):
    x = the_limit
    while x >= 1:
        print("*" * x)
        x -= 1 

def main():
    up_side_down_triangle(4)

if __name__ == "__main__":
    main()