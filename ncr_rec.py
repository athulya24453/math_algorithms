def ncr(n,k):
    if k == n or k == 0:
        return 1
    
    return ncr((n-1), (k-1)) + ncr((n-1), k)

print(ncr(153, 35))