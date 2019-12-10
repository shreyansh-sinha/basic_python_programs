def fact(n):
    f = 1
    x = 1
    while x <= n:
        f = f*x
        x += 1
    return f

t = int(input())

for _ in range(t):
    n = int(input())
    z = fact(n)
    print(z)
