# hw: wtp to check if a number is multiple of 64
def divisible_by_number(num):
    if num & 63 == 0:
        return True
    else:
        return False

def main():
    number = 128
    if divisible_by_number(number):
        print("The number {} is divisble by 64".format(number))
    else:
        print("The number {} is not divisble by 64".format(number))

if __name__ == "__main__":
    main()
