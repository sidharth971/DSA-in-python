'''
@Sidharth Sahoo
Insertion sort and modified bubble sort.
'''


def insertion_sort(__lst: list) -> list:
    '''
    Insertion sort implementation
    '''
    for i in range(1, len(__lst)):
        temp = __lst[i]
        j = i - 1
        while j >= 0 and temp < __lst[j]:
            __lst[j + 1] = __lst[j]
            j -= 1
        __lst[j + 1] = temp

    return __lst


if __name__ == '__main__':
    lst = [3, 5, 1, 2, 7, 6, 8, 9]

    print(insertion_sort(lst))
