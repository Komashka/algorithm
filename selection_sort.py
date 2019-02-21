def selection_sort(lst):
    for i in range(len(lst)):
        min = i
        for j in range(i + 1, len(lst)):
            if lst[min] > lst[j]:
                min = j
        temp = lst[i]
        lst[i] = lst[min]
        lst[min] = temp

    return lst
