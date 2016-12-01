def hanoi(n, i=1, k=2):
    if n == 1:
        print(n, i, k)
    else:
        tmp = 6 - i - k
        hanoi(n-1, i, tmp)
        print(n, i, k)
        hanoi(n-1, tmp, k)
hanoi(10)