def perfect_triangle():
    alpha_list = "ABCDEFG"
    x, y = len(alpha_list), 1
    spaces = len(alpha_list) - 1

    while y <= x:
        print(" " * spaces + alpha_list[y-1:0:-1]+alpha_list[:y])
        y += 1
        spaces -= 1

def right_angle_triangle():
    alpha_list = "ABCDE"

    for x in range(1,len(alpha_list) + 1):
        print(alpha_list[:x])

def main():
    print("Perfect Symmetrical Alphabet Triangle: ")
    perfect_triangle()
    print("Right Angled Alphabet Triangle: ")
    right_angle_triangle()

if __name__ == "__main__":
    main()