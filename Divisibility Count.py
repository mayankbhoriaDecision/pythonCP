import math

MOD = 1000000007


def sub(x, y):
    return (x - y + MOD) % MOD


def mul(x, y):
    return (x * y) % MOD


def power(x, y):
    res = 1
    x %= MOD
    while y != 0:
        if y & 1:
            res = mul(res, x)
        y >>= 1
        x = mul(x, x)

    return res


def mod_inv(n):
    return power(n, MOD - 2)


x, y = [int(i) for i in input().split()]

m = math.lcm(x, y)
n = int(input())
a = -1
b = -1
total = 1
for i in range(n - 1):
    total = (total * 10) % m
b = total % m
total = (total * 10) % m
a = total % m

l = power(10, n - 1)
r = power(10, n)

ans = sub(sub(r, l), sub(a, b))
ans = mul(ans, mod_inv(m))

print(ans)
