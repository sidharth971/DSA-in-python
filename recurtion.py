'''
@Sidharth Sahoo
Recursion is a process in which a function call itself again and again
to solve a problem.
'''


def factorial(n):
    '''
    output: 3628800
    '''
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def printN(n):
    '''
    output: 1 2 3 4 5 6 7 8 9 10
    '''
    if n > 0:
        printN(n - 1)
        print(n, end=' ')


def printNreverse(n):
    '''
    output: 10 9 8 7 6 5 4 3 2 1
    '''
    if n > 0:
        print(n, end=' ')
        printNreverse(n - 1)


def printoddnumbers(n):
    '''
    output: 1 3 5 7 9 11 13 15 17 19
    '''
    if n > 0:
        printoddnumbers(n - 1)
        print(2 * n - 1, end=' ')


def printevennumbers(n):
    '''
    output: 2 4 6 8 10 12 14 16 18
    '''
    if n > 0:
        printevennumbers(n - 1)
        print(2 * n, end=' ')


def printevennumbersreverse(n):
    '''
    output: 18 16 14 12 10 8 6 4 2
    '''
    if n > 0:
        print(2 * n, end=' ')
        printevennumbersreverse(n - 1)


def printoddnumbersreverse(n):
    '''
    output: 19 17 15 13 11 9 7 5 3 1
    '''
    if n > 0:
        print(2 * n - 1, end=' ')
        printoddnumbersreverse(n - 1)


def sumofnaturalnumber(n):
    '''
    output: 55
    '''
    if n == 0:
        return 0
    return n + sumofnaturalnumber(n - 1)


def sumofnaturalnumberodd(n):
    '''
    output: 25
    '''
    if n == 0:
        return 0
    return 2 * n - 1 + sumofnaturalnumberodd(n - 1)


def sumofnaturalnumbereven(n):
    '''
    output: 30
    '''
    if n == 0:
        return 0
    return 2 * n + sumofnaturalnumbereven(n - 1)


def squere(n):
    '''
    output: 144
    '''
    if n == 0:
        return 0
    return n * n + squere(n - 1)


if __name__ == "__main__":
    print(factorial(10))
    printN(10)
    print()
    printNreverse(10)
    print()
    printoddnumbers(10)
    print()
    printevennumbers(10)
    print()
    printevennumbersreverse(10)
    print()
    printoddnumbersreverse(10)
    print()
    print(sumofnaturalnumber(10))
    print(sumofnaturalnumberodd(10))
    print(sumofnaturalnumbereven(10))
    print(squere(10))
