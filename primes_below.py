def primes_below(n):
    l=[]
    for n in range (1,n):
        if n > 1:
            for i in range (2,n):
                if n % i == 0:
                    break
            else:
                l.append(n)
    return l

print(primes_below(8))