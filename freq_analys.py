N = int(input())
names = input().split()
A = [-1 for i in range(N)]
for i in range(N):
    k = names[:i+1].count(names[i])
    if names[:i+1].count(names[i]) == 1:
        A[i] = k + names[i+1:].count(names[i])
m, k = max(A), 0
for i in A:
    if k < i < m:
        k = i
print(A.count(k))