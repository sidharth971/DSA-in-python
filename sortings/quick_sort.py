'''
@Sidharth Sahoo
Quick sort and modified bubble sort.
'''


def quick_sort(__lst: list) -> list:
    '''
    Quick sort implementation
    '''
    if len(__lst) <= 1:
        return __lst

    pivot = __lst[0]
    left = [elem for elem in __lst if elem < pivot]
    right = [elem for elem in __lst if elem > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    lst = [3, 5, 1, 2, 7, 6, 8, 9]

    print(quick_sort(lst))
