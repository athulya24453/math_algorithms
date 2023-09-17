# Primes within the interval [2,n]

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

    return s_arr, sf_arr

ans_arr, ansf_arr = sieve(100)

print(ans_arr[37]) # prints 0 if 37 is a prime. else prints 1
print(ansf_arr[77]) # prints the smallest prime factor of 77