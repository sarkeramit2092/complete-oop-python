class Fraction:

    def __init__(self, n, d):
        self.n = n
        self.d = d

    def __str__(self):
        return f"{self.n}/{self.d}"
    def __add__(self,other):
        temp_n = self.n * other.d + other.n * self.n
        temp_d = self.d * other.d
        return f"{temp_n}/{temp_d}"
    def __sub__(self,other):
        temp_n = self.n * other.d - other.n * self.d
        temp_d = self.d * other.d
        return f"{temp_n}/{temp_d}"
    def __mul__(self,other):
        temp_n = self.n * other.n
        temp_d = self.d * other.d
        return f"{temp_n}/{temp_d}"
    def __truediv__(self,other):
        temp_n = self.n * other.d
        temp_d = self.d * other.n
        return f"{temp_n}/{temp_d}"
    
x = Fraction(4,3)
y = Fraction(5,6)

print(x)
print(y)
print(x+y)
print(x/y)
print(x*y)