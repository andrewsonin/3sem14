def generation(cash=5, people=1, m=1):
    if people == 0 or cash < 5:
        return 0
    coins = cash // 5
    for i in range(coins + 1):
        m += generation(cash - 5*i, people - 1)
    return m
print(generation(15, 3))