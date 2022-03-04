import math

a = 1
b = 0
c = 1

def solve_quadratic(a,b,c):
    d = b * b - 4 * a * c
    sqrt_val = math.sqrt (abs(d))

    if d == 0:
        return (-b / (2 * a))
    elif d > 0:
        return ((-b + sqrt_val)/(2 * a), (-b - sqrt_val)/(2 * a))
    else: 
        return None

if a == 0: 
        print("a cannot equal 0")  
else:
    solve_quadratic(a, b, c)
