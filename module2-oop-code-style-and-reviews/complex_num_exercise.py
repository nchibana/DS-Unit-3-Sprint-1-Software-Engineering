class Complex:
    def __init__(self, realpart, imagpart):       
        self.r = realpart
        self.i = imagpart

    def __repr__(self):
        return '%s + %si' % (self.r, self.i)

    def add(self, realpart, imagpart):
        return Complex(self.r + realpart,
                       self.i + imagpart)

y = Complex(3,5)
v = y.add(2,4)
print(v)