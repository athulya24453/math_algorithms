def is_prime(n):
    k = 0
    if n**(1/2) % 1 == 0:
        return False
    
    for  i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            k += 1

    if k == 0:
        return True

print(is_prime(1))

        