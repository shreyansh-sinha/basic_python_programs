import math
def solve(f, g, h):
    d = math.sqrt(f*f - 4*g*h)
    x1 = (-g + d)/2*f
    x2 = (-g - d)/2*f
    return x1, x2

x1, x2 = solve(1, 3, -4)
print(x1)
print(x2)

