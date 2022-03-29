def big_fibonnaci(n):
    a=1
    b=1
    c = a + b
    
    while len(str(c)) < n:
        a = b
        b = c
        c = a + b
    return c

print(big_fibonnaci(15))