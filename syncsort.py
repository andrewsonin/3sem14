def syncsort(linked_list, list_for_sort):
    massive = sorted(tuple(zip(linked_list, list_for_sort)), key=lambda x: x[1])  # можно добавить параметр reverse. По ум. False
    lenmass = len(massive)
    for i in range(lenmass - 1):
        j = i
        while i != lenmass - 1 and massive[i][1] == massive[i+1][1]:
            i += 1
        massive[j:i+1] = sorted(massive[j:i+1], key=lambda x: x[0])
    return massive

A = [4, 54, 5, 3, 2, 8, 5, 56, 634, 44, 843, 23]
B = [32, 234, 234, 234, 22, 35, 33, 34, 3, 3, 233, 233]
print(syncsort(A, B))