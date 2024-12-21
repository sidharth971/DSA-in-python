'''
@Sidharth Sahoo
Bubble sort and modified bubble sort.
'''


class Bubble:
    '''
    This class contains bubble and modified bubble sort.
    '''

    @staticmethod
    def bubble_sort(__iterable: list) -> list:
        '''
        bubble sorting
        '''

        for i in range(len(__iterable)):
            for j in range(len(__iterable) - i - 1):
                if __iterable[j + 1] < __iterable[j]:
                    __iterable[j], __iterable[j + 1] = __iterable[j + 1], __iterable[j]

        return __iterable

    @staticmethod
    def modified_bubble_sort(__iterable: list) -> list:
        '''
        modified bubble sorting. This is faster tha bubble sort.
        '''

        for i in range(len(__iterable)):
            swap = False
            for j in range(len(__iterable) - i - 1):
                if __iterable[j + 1] < __iterable[j]:
                    swap = True
                    __iterable[j], __iterable[j + 1] = __iterable[j + 1], __iterable[j]
            if not swap:
                break
        return __iterable


if __name__ == '__main__':
    lst = [3, 5, 1, 2, 7, 6, 8, 9]

    bbl_sorting = Bubble()
    print(bbl_sorting.bubble_sort(lst))
    print(bbl_sorting.modified_bubble_sort(lst))
