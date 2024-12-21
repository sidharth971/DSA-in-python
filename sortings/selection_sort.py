'''
@Sidharth Sahoo
Selection sort and modified bubble sort.
'''


def selection_sort(__lst: list) -> list:
    '''
    Selection sort implementation
    '''
    n = len(__lst)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if __lst[j] < __lst[min_index]:
                min_index = j
        __lst[i], __lst[min_index] = __lst[min_index], __lst[i]

    return __lst


if __name__ == '__main__':
    lst = [3, 5, 1, 2, 7, 6, 8, 9]

    print(selection_sort(lst))
