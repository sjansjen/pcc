a = 1
b = 2

#hasil = a + b

def pertambahan(_a, _b):
    h = _a + _b
    return h

def perkalian(_a, _b):
    h = _a * _b
    return h

hasil = pertambahan(a, b)
hasil = perkalian(hasil, 2)

print (hasil)


class Matematika():
    
    def __init__(self, _a, _b):
        self.h = None
        self.a = _a
        self.b = _b
        
        self.hasil = self.pertambahan()
        self.hasil = self.perkalian()
        
    def pertambahan(self):
        h = self.a + self.b
        return h
        
    def perkalian(self):
        h = self.hasil * self.b
        return h
    
    def perkalian2(aa, bb):
        h = aa * bb
        return h

#Main Program
m = Matematika(1, 2)
m2 = Matematika(2, 4)

hasilTotal = m.perkalian(hasil)

print (m.hasil)
print (hasilTotal)
print (m2.hasil)