

def bigMod(A, N, M):
    if N == 1:
        return A % M
    else:
        temp = bigMod(A, N // 2, M) % M
        if N % 2 == 0:
            return ((temp % M) * (temp % M)) % M
        else:
            return ((A % M) * (temp % M) * (temp % M)) % M

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def eGcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return x0

p = 11
q = 19

n = p * q

phi_n = (p - 1) * (q - 1)

pubK = 0
for i in range(2, phi_n):
    if (gcd(i, phi_n) == 1):
        pubK = i
        break

K2 = 17
K1 = eGcd(K2, phi_n)

plainText = 1002
cipherText = bigMod(plainText, K2, n)
print("Cipher = ", cipherText, end="\n")

plainText1 = bigMod(cipherText, K1, n)
print("Plain = ", plainText1, end="\n")
print()


