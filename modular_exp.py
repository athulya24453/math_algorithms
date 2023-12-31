def mod_exp(x, n):
    # calculates x^n in O(log(n))

    if n == 0:
        return 1

    if n % 2 == 0:
        return mod_exp(x,n/2)*mod_exp(x,n/2)
    
    else:
        return mod_exp(x, n-1)*x
    
# print(mod_exp(512,83))

n = int(input())

for i in range(n):
    a,b = list(map(int, input().split(" ")))
    ans = (mod_exp(a,b)) % (10**9 + 7)
    print(ans)