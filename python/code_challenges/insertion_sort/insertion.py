def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min = i
        # print(min, 'min')
        for j in range(i+1, n):
            # print(j, 'jjj')
            if lst[j] < lst[min]:
                min = j
        temp = lst[min]
        lst[min] = lst[i]
        lst[i] = temp
        print(lst)
    return lst

print(selection_sort([20,18,12,8,5,-2]))
