def countDiv(n):
    count = 2

    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            count += 2

    if n**(1/2)%1 == 0:
        count -= 1

    return count

n = int(input())

for i in range(n):
    x = int(input())
    print(countDiv(x))