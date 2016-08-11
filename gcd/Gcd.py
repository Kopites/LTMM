# Eucluid and Extend Eucluid

# 1. Eucluid

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 2. Extend Euclid

def eGcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

print(gcd(12, 16))
print(eGcd(12, 16))

