def minprice(n, price):
    massive = [float('+inf'), price[1]] + [None]*(n-1)
    for i in range(2, n+1):
        massive[i] = price[i] + min(massive[i-1], massive[i-2])
    return massive[n]

n = int(input())
price = list(map(int, input().split()))
print(minprice(n, price))