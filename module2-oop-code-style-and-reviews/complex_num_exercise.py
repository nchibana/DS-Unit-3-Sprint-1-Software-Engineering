
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def __repr__(self):
        return '%s + %si' % (self.r, self.i)

    def add(self, realpart, imagpart):
        return (self.r + realpart,
                self.i + imagpart)