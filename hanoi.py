def hanoi(n, i=1, k=2):
    if i + k == 5:
        tmp = 6 - i - k
        hanoi(n, i, tmp)
        hanoi(n, tmp, k)
    else:
        if n == 1:
            print(n, i, k)
        else:
            tmp = 6 - i - k
            hanoi(n-1, i, tmp)
            print(n, i, k)
            hanoi(n-1, tmp, k)

hanoi(3)