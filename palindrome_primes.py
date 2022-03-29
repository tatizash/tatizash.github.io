def palindrome_primes(a,b):

    for n in range(a,b+1):
        c=0
        rev=0
        tmp=n

        for i in range(1,tmp+1):
            if tmp%i==0:
                c+=1
        if c==2:
            while tmp>0:
                rev=rev*10+(tmp%10)
                tmp//=10
            if rev==n:
                print (n, end=",")

print(palindrome_primes(100, 999))

#alternatively:
def is_prime(n):
    if n > 1:
        for i in range (2,n):
            if n % i == 0:
                return False
        return True
    else:
        return False

def palindrome_primes(a,b):
    l = []
    for i in range (a,b):
        if str(i) == str(i)[::-1]:
            if is_prime(i):
                l.append(i)
    return (l)

print(palindrome_primes(100,1000))