def gcd(a,b):
    if b == 0:
        return a
    
    return gcd(b, a % b)

def lcm(a,b):
    return a*b/gcd(a,b)

def extended_euclidean(a,b):
    # finds two integers x and y s.t. ax + by = gcd(a,b)

    if b == 0:
        return (1,0,a)
    
    if a == 0:
        return (0,1,b)
    
    x, y, g = extended_euclidean(b, a%b)
    
    x_dash = y
    y_dash = x - int(a/b)*y
    return (x_dash, y_dash, g)

def diaphanton_eqns(a,b,c):
    if c % gcd(a,b) != 0:
        print("No solutions")
        return
    
    ans = extended_euclidean(a,b)

    fac = c/gcd(a,b)

    return (ans[0]*fac, ans[1]*fac)

print(gcd(15,11))
print(lcm(12,36))
print(extended_euclidean(24,36))
print(diaphanton_eqns(39, 15, 12))