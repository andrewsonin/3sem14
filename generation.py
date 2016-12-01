def generation(n=5, k=1, m=0):
    if k == 0 or n < 5:
        return 0
    quantity = n // 5
    for i in range(quantity + 1):
        if m == 0:
            m += 1
        m += generation(n - i, k - 1)
    return m
print(generation(15, 2))