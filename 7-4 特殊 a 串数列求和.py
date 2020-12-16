def create_num(a, n):
    res = 0
    for i in range(0, n):
        res *= 10;
        res += a;
    return res

a, n = map(int, input().split())
sum = sum([create_num(a, i) for i in range(1, n + 1)])
print("s = %d" %sum)