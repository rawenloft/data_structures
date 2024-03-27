def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
        
        m = old_n
        n = old_m % old_n
    return n

class Fraction:
    
    def __init__(self, top, bottom):
        if bottom == 0:
            raise ValueError("Denominator must not be zero.")
        self.num = top
        self.den = bottom
        
    def __str__(self):
        if self.num == 0:
            return "0"
        elif self.num == self.den:
            return "1"
        elif self.num > self.den:
            main = self.num // self.den
            self.num = self.num - (main * self.den)
            return "{}_{}/{}".format(main, self.num, self.den)
        return "{}/{}".format(self.num, self.den)
    
    def show(self):
        print(self.num, "/", self.den)
    
    def invert(self, fraction):
        return Fraction(fraction.den, fraction.num)
    
    def __add__(self, other_fraction):
        newnum = self.num * other_fraction.den + self.den * other_fraction.num
        newden = self.den * other_fraction.den
        common = gcd(newnum, newden)
        
        return Fraction(newnum // common, newden // common)
    
    def __eq__(self, other):
         first_num = self.num * other.den
         second_num = other.num * self.den
         
         return first_num == second_num   
    
    def __sub__(self, other_fraction):
        return self + Fraction(- other_fraction.num, other_fraction.den)
    
    def __truediv__(self, fraction):
        inverted_fraction = self.invert(fraction)
        return self * inverted_fraction
    
    def __mul__(self, other_fraction):
        newnum = self.num * other_fraction.num
        newden = self.den * other_fraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)
    
    def __repr__(self) -> str:
        return "{}/{}".format(self.num, self.den)
    
x = Fraction(5,7)

y = Fraction(5,7)

res = x + y
print(res)
print(x - y)
print(x * y)
print(x / y)
print( x == y)