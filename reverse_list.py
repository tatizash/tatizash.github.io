l = ["cat","dog","parrot","hamster","turtle","fish","ferret","chameleon"]

def my_reverse(l):
    l2=[]
    x = len(l)
    while x > 0:
        l2.append(l[x - 1])
        x = x - 1
    return l2

print(my_reverse(l))