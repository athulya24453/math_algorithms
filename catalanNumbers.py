def ncr(n,k):
    if k == n or k == 0:
        return 1
    
    return ncr((n-1), (k-1)) + ncr((n-1), k)

def catalanNum(n: int) -> int:
    return int((1/(n+1))*ncr(2*n, n))

print(catalanNum(4))