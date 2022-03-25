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
                print(n, end=",")

print(palindrome_primes(100, 999))