def gcd(a, b):
    """returns gcd of two values"""
    while(a != 0 and b != 0):
        if(a >= b):
            a = a % b
        else:
            b = b % a
    return a + b

#collection of test funcs   
def prime_test(a):
    """test of 'a' for being a prime"""
    for i in range(2, a):
        if a % i == 0:
            return False
    return True
def coprime_test(a, b):
    """test if two values are coprime to each other"""
    while(a != 0 and b != 0):
        if(a >= b):
            a = a % b
        else:
            b = b % a
    
    if (a + b) == 1:
        return True
    else:
        return False
def group_prime_test(p, q, e):
    """combination of 3 tests for prime number + coprime test of p and q"""
    for var in (p, q, e):
        if not prime_test(var):
            return False
    if not coprime_test(p, q):
        return False
    return True
    
    
def find_coprime(a, number=1):
    """Function which takes as an input prime number "a" and return coprime to "a". By default return one coprime. 
    If passed with non-default value of "number", eg 5, then returns a list of 5 coprimes"""
    b = 2
    res = []
    
    while (len(res) < number): 
        if gcd(a, b) == 1 and prime_test(b):
            res.append(b)
            b += 1
        else:
            b += 1
            
    return res

def find_d(e, phi_n):
    """Function which searchs (brute force) for d (secret key), which will sutisfy condition e * d = 1 mod phi_n"""
    d = 2
    
    for i in range(100000):
        if prime_test(d) and gcd(e, d) == 1:
            if (e * d) % phi_n == 1:
                return d
            d += 1
        else:
            d += 1
    
    return False


p = 102639592829741105772054196573991675900716567808038066803341933521790711307779
q = 106603488380168454820927220360012878679207958575989291522270608237193062808643

n = p * q 
phi_n = (p - 1) * (q - 1) 

e = 3
d = 7294492427713684947873138214693571741335821963632803993942561420984233322859150361091191565553782900720461165563467939513795006590467689467848406386811651

# encryption approved
x = 50
print("Encrypting message '{}'...".format(x))

y = (x ** e) % n
print("Encrypted: {}\n".format(y))
print("Decrypting message '{}'...".format(y))
print("Decrypted: {}\n".format((y ** d) % n))
        
        
"""
p = 5
q = 11
n = p * q 
phi_n = (p - 1) * (q - 1) 
print("phi = {}".format(phi_n))

print("Computing e...")
e = find_coprime(phi_n)[0]
print("Done: e = {}\n".format(e))

#check 3 selected variables
print("Check 3 variables: p, q, e: ", end='')
print(group_prime_test(p, q, e))

# check if e and Phi are coprime. If so, find d
if coprime_test(e, phi_n):
    print("\nComputing d...")

    d = find_d(e, phi_n)
    if d:
        print("Done: d = {}\n".format(d))
        
        # encryption approved
        x = 50
        print("Encrypting message '{}'...".format(x))
    
        y = (x ** e) % n
        print("Encrypted: {}\n".format(y))
        print("Decrypting message '{}'...".format(y))
        print("Decrypted: {}\n".format((y ** d) % n))
                
    else:
        print("Fail to compute d: no such value within defined range\n")
else:
    print("Fail: e({0}) and phi_n ({1}) are not coprime".format(e, phi_n))
    
"""