def gcd(a,b):
    if b == 0:
        return a
    
    return gcd(b, a % b)

def max_gcd(l: list) -> int:
    m = max(l)
    ans = 1

    for i in range(2,m+1):
        for j in range(len(l)):
            for k in range(j+1, len(l)): 
                if l[j]%i == 0 and l[k]%i == 0:
                    ans = i

    return ans

n = int(input())
li = list(map(int, input().split(" ")))

print(max_gcd(li))