l=[]
m=5
n=22

def my_range(m,n):
    while m <= n:
        l.append(m)
        m = m + 1
        print(l)

print(my_range(m,n))