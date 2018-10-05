def primes(n): #решето Эратосфена
    a = [0] * n 
    for i in range(n): 
        a[i] = i 
    a[1] = 0
     
    p = 2 
    while p < n: 
        if a[p] != 0: 
            j = p * 2 
            while j < n:
                a[j] = 0 
                j = j + p 
        p += 1
     
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    return b
print(primes(20))
    
