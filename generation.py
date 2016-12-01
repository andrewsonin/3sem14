def generation(cash=5, people=1, m=1):
    if people == 0:
        return 0
    quantity = cash // 5
    for i in range(quantity + 1):
        m += generation(cash - i, people - 1)
    return m
print(generation(15, 2))