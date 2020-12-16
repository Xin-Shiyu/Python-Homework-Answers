i = 1;
while True:
    if i % 5 == 1 and i % 6 == 5 and i % 7 == 4 and i % 11 == 10:
        print(i)
        break
    i += 1