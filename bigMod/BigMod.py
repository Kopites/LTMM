def bigMod(A, N, M):
    if N == 1:
        return A % M
    else:
        temp = bigMod(A, N // 2, M) % M
        if N % 2 == 0:
            return ((temp % M) * (temp % M)) % M
        else:
            return ((A % M) * (temp % M) * (temp % M)) % M


print(bigMod(101, 17, 209))
print(bigMod(73, 53, 209))
