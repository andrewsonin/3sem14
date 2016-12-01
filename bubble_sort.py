def bubble(B):
    A, s = B[0:], 0
    for k in range(1, len(A)):
        for i in range(len(A)-k):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                s += 1
    return s