# hw: wtp to accept a number from user, accept a bit position which should be turned off from the given number

def turn_off_bit(number, bit_pos):
    x = 1
    x = x << (bit_pos - 1)
    x = ~x

    return number ^ x

def main():
    number = eval(input("Enter your number: "))
    bit = eval(input("Enter bit to turn off: "))
    print("For number {} when bit number {} is turned off, the result is: {}".format(number, bit, turn_off_bit(number,bit)))

if __name__ == "__main__":
    main()