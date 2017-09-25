def gcd(a, b):
    """returns gcd of two values"""
    while(a != 0 and b != 0):
        if(a >= b):
            a = a % b
        else:
            b = b % a
    return a + b

#added line
