class Triangle():
    def __init__(self,a,b,c):
        self.side_a = a
        self.side_b = b
        self.side_c = c

    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return (s*(s-self.side_a)*(s-self.side_b)*(s-self.side_c))**0.5

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def scale(self, scale_factor):
        return Triangle(scale_factor * self.side_a, scale_factor * self.side_b, scale_factor * self.side_c)

    def is_valid(self):
        if (self.side_a + self.side_b < self.side_c) or (self.side_a + self.side_c < self.side_c) or (self.side_b + self.side_c < self.side_a) :
            return False
        else:
            return True  
    
    def is_right(self):
        if (self.side_a**2 + self.side_b**2 == self.side_c**2) or (self.side_c**2 + self.side_b**2 == self.side_a**2) or (self.side_a**2 + self.side_c**2 == self.side_b**2) :
            return True 
        else:
            return False

t = Triangle(7,12,15)

print("Area = %d" % t.area())

print ("Perimeter = %d" % t.perimeter())

m = t.scale(3)
print(m.side_a, m.side_b, m.side_c)

print (t.is_valid())

print (t.is_right())