def gcd(a, b):
    """returns"""
    while(a != 0 and b != 0):
        if(a >= b):
            a = a % b
        else:
            b = b % a
    return a + b

"""new comment"""
#added line

def test(a, b):
    """returns"""