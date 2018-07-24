# WH: WAP to represent a complex number and perform following methods:
# Add two complex, subtract, add constant to complex number, compare two complex numbers (==, <=, >=, !=, <, >)
# Make it menu driven

class Complex_number:

    """ For creating objects of complex numbers and performing addition and subtraction operations.
    Also, we can use this for comparision of two complex numbers. It performs all comparisions. """

    def __init__(self, real, imaginary):

        if type(real) not in [int, float] and type(imaginary) not in [int, float]:
            print("Real and Imaginary parts must be Integers or Float")
            return 

        self.real = real
        self.imaginary = imaginary

    # This function is called when we print the object
    def __repr__(self):
        return self.real + self.imaginary * 1j

    def modulus(self):
        return (self.real**2 + self.imaginary**2) ** 0.5
    
    def __add__(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return real_part + imaginary_part * 1j

    def __sub__(self, other):
        real_part = self.real - other.real
        imaginary_part = self.imaginary - other.imaginary
        return real_part + imaginary_part * 1j

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __lt__(self, other):
        return self.modulus() < other.modulus()

    def __le__(self, other):
        return self.modulus() <= other.modulus()

    def __gt__(self, other):
        return self.modulus() > other.modulus()

    def __ge__(self, other):
        return self.modulus() >= other.modulus()

    def __ne__(self, other):
        return self.real != other.real and self.imaginary != other.imaginary

def main():
    real1 = eval(input("Enter real part of first number: "))
    imaginary1 = eval(input("Enter imaginary part of first number: "))
    real2 = eval(input("Enter real part of first number: "))
    imaginary2 = eval(input("Enter imaginary part of first number: "))

    number1 = Complex_number(real1, imaginary1)
    number2 = Complex_number(real2, imaginary2)

    while True:
        print("Which operation do you want to perform?")
        print("1. Display all the complex numbers")
        print("2. Check if they are equal")
        print("3. Check if first number is greater than second")
        option = eval(input("Enter your option: "))

        if option == 1:
            print("{} and {} are your complex numbers".format(number1, number2))
        elif option == 2:
            if number1 == number2:
                print("Both complex numbers are same")
            elif number1 != number2:
                print("Both complex numbers are different")
        elif option == 3:
            if number1 > number2:
                print("{} is greater than {}".format(number1, number2))
            elif number2 > number1:
                print("{} is greater than {}".format(number2, number1))
        else:
            print("Entered a different option, exiting...")
            break

if __name__ == "__main__":
    main()
