import math

a = 1
b = -5
c = 6

def solve_quadratic(a,b,c):
    d = b * b - 4 * a * c
    sqrt_val = math.sqrt (abs(d))

    if d == 0:
        print (-b / (2 * a))
    elif d > 0:
        print ((-b + sqrt_val)/(2 * a), (-b - sqrt_val)/(2 * a))
    else: 
        print("None")

if a == 0: 
        print("a cannot equal 0")  
else:
    solve_quadratic(a, b, c)
