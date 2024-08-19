import math

def cplxsum(a, b):
    real = a[0] + b[0]
    img  = a[1] + b[1]
    return (real, img)

def cplxprod(a, b):
    real = a[0]*b[0] - a[1]*b[1]
    img  = a[0]*b[1] + a[1]*b[0]
    return (real, img)

def cplxrest(a, b):
    real = a[0] - b[0]
    img  = a[1] - b[1]
    return (real, img)

def cplxdiv(a, b):
    real = (a[0]*b[0] + a[1]*b[1]) / (b[0]**2 + b[1]**2)
    img  = (a[1]*b[0] - a[0]*b[1]) / (b[0]**2 + b[1]**2)
    return (real, img)  

def cplxmod(a):
    modulo = (a[0]**2 + a[1]**2)**0.5
    return modulo

def cplxfase(a):
    fase = math.atan2(a[1], a[0])
    return fase

def cplxconj(a):
    real = a[0]
    img = -a[1]
    return (real, img)

def polcplx(a):
    real = a[0]*math.cos(a[1])
    img = a[0]*math.sin(a[1])
    return (real, img)


def cplxpol(a):
    modulo = cplxmod(a)
    fase = cplxfase(a)
    return (modulo, fase)

if __name__ == "__main__":
    a1 = (1, 2)
    b1 = (3, 4)
    print(cplxsum(a1, b1))
    print(cplxprod(a1, b1))
    print(cplxrest(a1, b1))
    print(cplxdiv(a1, b1))
    print(cplxmod(a1))
    print(cplxfase(a1))
    print(cplxconj(a1))
    a2 = (3, math.pi/4)
    print(polcplx(a2))
    print(cplxpol(a1))
    a3 = (5, 6)
    b3 = (2, 3)
    print(cplxsum(a3, b3))
    print(cplxprod(a3, b3))
    print(cplxrest(a3, b3))
    print(cplxdiv(a3, b3))
    print(cplxmod(a3))
    print(cplxfase(a3))
    print(cplxconj(a3))
    a4 = (4, math.pi/3)
    print(polcplx(a4))
    print(cplxpol(a3))