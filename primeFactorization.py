def sieve(n):
    s_arr = [0 for i in range(n+1)]
    sf_arr = [0 for i in range(n+1)]

    for i in range(2,n+1):
        if s_arr[i]:
            continue

        for j in range(2*i, n+1, i):
            s_arr[j] = 1
            if sf_arr[j] == 0:
                sf_arr[j] = i 

    return s_arr

def prime_fac(n):
    p_arr = sieve(n)
    fac_arr = []
    exp_arr = []

    for i in range(2,int(n/2)+1):
        if not p_arr[i]:
            count = 0
            while n % i == 0:
                count += 1
                n = n/i

            else:
                fac_arr.append(i)
                exp_arr.append(count)

    return fac_arr, exp_arr

factors, exp = prime_fac(19)
print(factors)
print(exp)

            

            