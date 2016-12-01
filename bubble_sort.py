def bubble(B):
    A, k = B[0:], 0
    for k in range(1, len(A)):
        for i in range(len(A)-k):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                k += 1
    return k