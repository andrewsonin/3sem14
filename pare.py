a, A, i = input().split(), [], 0
while a != ['0', '0']:
    a[0], a[1] = int(a[0]), int(a[1])
    if a[0] // 2 == 0 and a[1] // 7 == 0 and (a[0] // 100 != 0 or a[1] // 100 != 0):
        i += 1
    a = input().split()
print(i)