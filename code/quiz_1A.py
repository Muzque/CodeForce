n, m, a = map(int, input().split())
L = n//a
if n % a > 0:
    L += 1
W = m//a
if m % a > 0:
    W += 1
print(L*W)
