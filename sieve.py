# Primes within the interval [2,n]

def sieve(n):
    s_arr = [0 for i in range(n+1)]

    for i in range(2,n+1):
        if s_arr[i]:
            continue

        for j in range(2*i, n+1, i):
            s_arr[j] = 1

    return s_arr

ans_arr = sieve(100)

print(ans_arr[37]) # prints 0 if 37 is a prime. else prints 1