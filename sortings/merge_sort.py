'''
@Sidharth Sahoo
Merge sort and modified bubble sort.
'''


def merge_sort(__lst: list) -> list:
    '''
    Merge sort implementation
    '''
    if len(__lst) > 1:
        mid = len(__lst) // 2
        left = __lst[:mid]
        right = __lst[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                __lst[k] = left[i]
                i += 1
            else:
                __lst[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            __lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            __lst[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    lst = [3, 5, 1, 2, 7, 6, 8, 9]

    merge_sort(lst)
    print(lst)
