def shellSort(lst):
    gap = len(lst) // 2
    while gap > 0:
        for i in range(gap, len(lst)):
            curr = lst[i]
            j = i
            while j >= gap and lst[j - gap] > curr:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = curr
        gap = gap// 2
    return lst
