def ncr(n,k):
    if k == n or k == 0:
        return 1
    
    return ncr((n-1), (k-1)) + ncr((n-1), k)

def ncr_mod(n,k):
    if k < n/2:
        num = 1
        for i in range(n-k+1, n+1):
            num *= i % (10**9+7)
        
        num_dash = num % (10**9+7)

        den = 1
        for i in range(1,k+1):
            den *= i %(10**9+7)

        den_dash = den % (10**9+7)
        inv_den_dash = den_dash**((10**9+7)-2)

        return num_dash*inv_den_dash

    else:
        num = 1
        for i in range(k+1, n+1):
            num *= i % (10**9+7)
        
        num_dash = num % (10**9+7)

        den = 1
        for i in range(1,n-k+1):
            den *= i %(10**9+7)

        den_dash = den % (10**9+7)
        inv_den_dash = den_dash**((10**9+7)-2)

        return num_dash*inv_den_dash

# print(ncr(21, 8)%(10**9+7))
print(ncr_mod(10, 3))