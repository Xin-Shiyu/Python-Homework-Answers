n = int(input())

for i in range(1, n + 1):
    j = 1
    while j < i:
        print("%4d" %j, end='')
        j += 1
    k = j
    while k <= n:
        print("%4d" %j, end='')
        k += 1
    print('')
