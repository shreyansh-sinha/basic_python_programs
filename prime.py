def is_prime(x):
    if x == 1:
        return False
    if x == 2 or x == 3:
        return True
    s = 2
    while s*s <= x:
        if x%s == 0:
            return False
        s += 1
    return True

def prime(n):
    x = 1
    while x <= n:
        if is_prime(x):
            print(x)
        x += 1
n = int(input())
prime(n)
