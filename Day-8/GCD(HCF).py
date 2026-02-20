def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

print(gcd(15,50))

# there is no efficient way to find the LCM . We can find the LCM using the GCD. The formula is LCM(a,b) = (a*b)/GCD(a,b)

def lcm(a,b):
    return (a*b)//gcd(a,b)
print(lcm(15,50))