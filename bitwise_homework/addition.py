def addition(a, b):
    
    while b!=0:
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a

print(addition(200,1))