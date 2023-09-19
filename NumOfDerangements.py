def derangements(n):
    if n == 1: 
        return 0
    
    if n == 2: 
        return 1
    
    return (n-1)*(derangements(n-1)+derangements(n-2))

print(derangements(3))