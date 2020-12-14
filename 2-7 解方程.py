import math

a, b, c = map(int, input("").split(" "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("no real solution")
elif delta == 0:
    x = -b / (2 * a)
    print("x=%.3f" %x)
else:
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print("x1=%.3f" %x1)
    print("x2=%.3f" %x2)